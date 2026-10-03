#!/usr/bin/env python3
"""
ODRR-RR-001 deterministic target-control matcher.
Uses only pre-outcome image features and declared source metadata.
"""
import argparse
import numpy as np
import pandas as pd

HIST=[f"orientation_hist_bin_{i}" for i in range(8)]
DIST_FEATURES=[
    "log_aspect_ratio","mean_luma_norm","rms_contrast_norm","entropy_bits",
    "edge_density_grad20","mean_gradient_norm","orientation_anisotropy",*HIST
]


def js_divergence(p,q):
    p=np.asarray(p,float); q=np.asarray(q,float)
    p=p/(p.sum()+1e-12); q=q/(q.sum()+1e-12)
    m=.5*(p+q)
    def kl(a,b):
        mask=a>0
        return float(np.sum(a[mask]*np.log2(a[mask]/(b[mask]+1e-12))))
    return .5*kl(p,m)+.5*kl(q,m)


def safe_ratio(a,b):
    if abs(b)<1e-12:
        return 1.0 if abs(a)<1e-12 else np.inf
    return a/b


def eligible(t,c):
    if t.source_class!=c.source_class: return False,"source_class"
    if t.render_mode!=c.render_mode: return False,"render_mode"
    if t.crop_scale_class!=c.crop_scale_class: return False,"crop_scale_class"
    ar=t.aspect_ratio/c.aspect_ratio
    if not (0.80<=ar<=1.25): return False,"aspect_ratio"
    if abs(t.mean_luma_norm-c.mean_luma_norm)>0.10: return False,"luminance"
    if abs(t.rms_contrast_norm-c.rms_contrast_norm)>0.10: return False,"contrast"
    if abs(t.entropy_bits-c.entropy_bits)>0.75: return False,"entropy"
    er=safe_ratio(t.edge_density_grad20,c.edge_density_grad20)
    if not (0.75<=er<=1.33): return False,"edge_density"
    gr=safe_ratio(t.mean_gradient_norm,c.mean_gradient_norm)
    if not (0.75<=gr<=1.33): return False,"gradient"
    js=js_divergence([getattr(t,h) for h in HIST],[getattr(c,h) for h in HIST])
    if js>0.20: return False,"orientation_hist_jsd"
    return True,""


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("features_csv")
    ap.add_argument("matches_csv")
    ap.add_argument("--audit_csv",default=None)
    args=ap.parse_args()
    df=pd.read_csv(args.features_csv)
    targets=df[df.kind=="target"].sort_values("source_id").copy()
    controls=df[df.kind=="control"].sort_values("source_id").copy()
    audit=[]; candidates={}
    for t in targets.itertuples(index=False):
        ids=[]
        for c in controls.itertuples(index=False):
            ok,reason=eligible(t,c)
            audit.append({"target_id":t.source_id,"control_id":c.source_id,"eligible":ok,"reject_reason":reason})
            if ok: ids.append(c.source_id)
        candidates[t.source_id]=ids

    X=df[DIST_FEATURES].astype(float)
    mu=X.mean(); sd=X.std(ddof=0).replace(0,1)
    Z=(X-mu)/sd
    zmap={sid:Z.iloc[i].to_numpy(float) for i,sid in enumerate(df.source_id)}

    used=set(); matches=[]
    for t in targets.itertuples(index=False):
        avail=[cid for cid in candidates[t.source_id] if cid not in used]
        if len(avail)<1:
            matches.append({"target_id":t.source_id,"control_id":"","distance":"","status":"NO_ELIGIBLE_UNUSED_CONTROL"})
            continue
        scored=sorted((float(np.linalg.norm(zmap[t.source_id]-zmap[cid])),cid) for cid in avail)
        dist,cid=scored[0]
        used.add(cid)
        matches.append({"target_id":t.source_id,"control_id":cid,"distance":dist,"status":"MATCHED"})
    pd.DataFrame(matches).to_csv(args.matches_csv,index=False)
    if args.audit_csv:
        pd.DataFrame(audit).to_csv(args.audit_csv,index=False)


if __name__=="__main__":
    main()
