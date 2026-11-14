#!/usr/bin/env python3
"""
ODRR-RR-001 objective image-feature extractor.
Pre-outcome tool. Does not read participant outcomes.

Input CSV columns:
source_id,path,source_class,render_mode,crop_scale_class,kind
where kind is target or control.
"""
from pathlib import Path
import argparse, math
import numpy as np
import pandas as pd
from PIL import Image, ImageOps


def entropy_gray(arr):
    hist=np.bincount(arr.ravel(), minlength=256).astype(float)
    p=hist/hist.sum()
    p=p[p>0]
    return float(-(p*np.log2(p)).sum())


def features(im):
    im=ImageOps.exif_transpose(im).convert("RGB")
    g=np.asarray(im.convert("L"),dtype=np.float32)
    mean=float(g.mean()/255.0)
    contrast=float(g.std()/255.0)
    gy,gx=np.gradient(g)
    mag=np.hypot(gx,gy)
    edge=float((mag>=20.0).mean())
    grad=float(mag.mean()/255.0)
    theta=np.mod(np.arctan2(gy,gx),np.pi)
    bins=np.linspace(0,np.pi,9)
    hist,_=np.histogram(theta,bins=bins,weights=mag)
    hist=hist.astype(float)
    hist=hist/hist.sum() if hist.sum()>0 else hist
    anis=float((np.mean(np.abs(gx))-np.mean(np.abs(gy)))/(np.mean(np.abs(gx))+np.mean(np.abs(gy))+1e-12))
    out={
        "width":im.width,"height":im.height,
        "aspect_ratio":im.width/im.height,
        "log_aspect_ratio":math.log(im.width/im.height),
        "mean_luma_norm":mean,
        "rms_contrast_norm":contrast,
        "entropy_bits":entropy_gray(g.astype(np.uint8)),
        "edge_density_grad20":edge,
        "mean_gradient_norm":grad,
        "orientation_anisotropy":anis,
    }
    out.update({f"orientation_hist_bin_{i}":float(v) for i,v in enumerate(hist)})
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("manifest_csv")
    ap.add_argument("output_csv")
    args=ap.parse_args()
    m=pd.read_csv(args.manifest_csv)
    req={"source_id","path","source_class","render_mode","crop_scale_class","kind"}
    missing=req-set(m.columns)
    if missing:
        raise SystemExit(f"Missing columns: {sorted(missing)}")
    rows=[]
    for r in m.to_dict("records"):
        im=Image.open(r["path"])
        rows.append({k:r[k] for k in ["source_id","source_class","render_mode","crop_scale_class","kind"]}|features(im))
    pd.DataFrame(rows).to_csv(args.output_csv,index=False)


if __name__=="__main__":
    main()
