"""Integridade formal somente: nenhuma validacao pedagogica."""
import json, hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent

def load(name):
    return json.loads((BASE/name).read_text(encoding="utf-8-sig"))

def pointer(root,path):
    for part in path.strip("/").split("/"):
        root=root[int(part)] if isinstance(root,list) else root[part.replace("~1","/").replace("~0","~")]
    return root

def citations(value):
    if isinstance(value,dict):
        if "kind" in value and "quote" in value: yield value
        for child in value.values(): yield from citations(child)
    elif isinstance(value,list):
        for child in value: yield from citations(child)

def check_rules(data,maximum=3):
    rows=[]
    for x in data["items"]:
        pairs={(l["oc_id"],l["competency_id"]) for l in x["links"]}
        pair_nodes={n for pair in pairs for n in pair}
        orphan=set(x["object_alignment"]["supported_oc_ids"])-{a for a,b in pairs}
        nodes=pair_nodes|orphan
        status="incomplete_mapping" if orphan else ("not_applicable" if not nodes else ("within_provisional_limit" if 1<=len(nodes)<=maximum else "review_limit_exceeded"))
        rows.append(dict(item_id=x["item_id"],pair_count=len(pairs),pair_node_count=len(pair_nodes),objects_without_pair=sorted(orphan),identified_node_count=len(nodes),status=status,limit_exceeded=len(nodes)>maximum))
    return dict(premise="manager_provisional_unique_OC_plus_COMP_1_to_3",maximum=maximum,orphan_policy="Count supported OC as one identified node, report incomplete_mapping; never invent COMP or truncate.",pedagogical_approval=False,items=rows)

def validate(packet,data,verify_hashes=True):
    errors=[]
    def require(ok,msg):
        if not ok: errors.append(msg)
    originals={x["record_id"]:x["data"] for x in packet["items"]}
    matrix=packet["matrix"]["data"]
    ocs={o["id"]:o for c in matrix["componentes_curriculares"] for o in c["objetos_conhecimento"]}
    comps={c["id"]:c for c in matrix["competencias"]}
    require(len(data["items"])==6,"six items required")
    require(set(x["record_id"] for x in data["items"])==set(originals),"sample identity changed")
    require(data["authorship"]=="session_agent_authored" and data["api_integration_executed"] is False,"provenance")
    require(data["criterion_source"]=="user_criterion_v2" and data["decision_source"]=="agent_judgment","criterion versus decision")
    for x in data["items"]:
        rid=x["record_id"]
        require(x["item_snapshot"]==originals.get(rid),rid+" snapshot changed")
        require(x["item_id"]==originals.get(rid,{}).get("id"),rid+" item identity")
        require(x["human_review"]=="pending" and x["pedagogical_approval"] is False and x["readiness"]["ready"] is False,rid+" approval/readiness")
        require(x["decision_source"]=="agent_judgment" and x["criterion_source"]=="user_criterion_v2",rid+" decision source")
        require(x["user_coherence_review"]=="pending" and x["specialist_pedagogical_review"]=="pending" and x["use_issues_decision_source"]=="agent_judgment",rid+" review separation")
        require(x["readiness"]["status"] in ["held_for_specialist_review","held_missing_context","not_approved_pending_review"],rid+" readiness status")
        supported=x["object_alignment"]["supported_oc_ids"]
        require(all(o in ocs for o in supported),rid+" unknown OC")
        state=x["status"]
        require(state in ["suggested","object_supported_competency_pending","abstained"],rid+" status")
        require((state=="suggested")==bool(x["links"]),rid+" links/status")
        if state=="object_supported_competency_pending":require(bool(supported) and not x["links"] and x["competency_alignment"]["status"]=="pending",rid+" pending state")
        if state=="abstained":require(not supported and not x["links"],rid+" abstention state")
        if supported:require({e["kind"] for e in x["evidence"]}>={"item","matrix","ementa"},rid+" positive evidence classes")
        for l in x["links"]:
            o,c=l["oc_id"],l["competency_id"]
            require(o in supported and c in ocs.get(o,{}).get("competencias",[]),rid+" incompatible pair")
            require(bool(l.get("scope")) and l.get("status")=="suggested_partial",rid+" partial scope")
            require(all(h in {h["id"] for h in comps.get(c,{}).get("habilidades",[])} for h in l["skill_ids"]),rid+" skill")
            require({e["kind"] for e in l["evidence"]}>={"item","matrix","ementa"},rid+" link evidence")
        for e in citations(x):
            try:
                if e["kind"]=="item":
                    require(e["record_id"]==rid,rid+" cross-item citation")
                    actual=originals[e["record_id"]][e["field"]]
                elif e["kind"]=="matrix":
                    require(e["file"]==packet["matrix"]["source"]["file"],rid+" matrix file")
                    actual=pointer(matrix,e["pointer"])
                elif e["kind"]=="ementa":
                    source=next(t for t in packet["ementas"] if t["source"]["file"]==e["file"])
                    a,b=e["line_start"],e["line_end"]
                    require(1<=a<=b<=len(source["text"].splitlines()),rid+" line bounds")
                    actual="\n".join(source["text"].splitlines()[a-1:b])
                else: raise ValueError("unknown citation kind")
                require(bool(e["quote"]) and e["quote"]==actual,rid+" literal citation mismatch")
            except (KeyError,IndexError,StopIteration,TypeError,ValueError):errors.append(rid+" invalid citation")
    if verify_hashes:
        for name,expected in data["source_hashes"].items():require(hashlib.sha256((BASE/name).read_bytes()).hexdigest()==expected,"source modified: "+name)
    return dict(valid=not errors,errors=errors,scope="literal citations, statuses, identity and source integrity only; no semantic/pedagogical approval",api_integration_executed=False)

if __name__=="__main__":
    packet,data=load("sample_packet.json"),load("suggestions_v2.json")
    result=validate(packet,data)
    # Rechecking must not fail merely because the frozen reports already exist.
    # Print fresh checks; keep the recorded v2 reports unchanged.
    print(json.dumps({"validation":result,"rules":check_rules(data)},ensure_ascii=False))
    raise SystemExit(0 if result["valid"] else 1)
