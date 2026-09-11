#!/usr/bin/env python3
import csv
import hashlib
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def entropy_u8(gray):
    hist = np.bincount(gray.ravel(), minlength=256).astype(float)
    p = hist / hist.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


def features(path):
    raw = Path(path).read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    im = Image.open(path).convert("L")
    w, h = im.size
    scale = min(1.0, 512.0 / max(w, h))
    if scale < 1.0:
        im = im.resize((max(1, round(w * scale)), max(1, round(h * scale))))
    arr = np.asarray(im, dtype=float) / 255.0
    gx = np.diff(arr, axis=1)
    gy = np.diff(arr, axis=0)
    edge_strength = (float(np.mean(np.abs(gx))) + float(np.mean(np.abs(gy)))) / 2
    gray_u8 = np.asarray(im, dtype=np.uint8)
    return {
        "filename": Path(path).name,
        "sha256": sha,
        "aspect_ratio": w / h,
        "mean_luminance": float(arr.mean()),
        "rms_contrast": float(arr.std()),
        "edge_strength": edge_strength,
        "entropy_bits": entropy_u8(gray_u8),
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: image_features.py IMAGE [IMAGE ...]")
    fieldnames = ["filename", "sha256", "aspect_ratio", "mean_luminance", "rms_contrast", "edge_strength", "entropy_bits"]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()
    for path in sys.argv[1:]:
        writer.writerow(features(path))
