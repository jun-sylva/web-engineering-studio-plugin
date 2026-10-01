#!/usr/bin/env python3
import argparse
import base64
import html
import json
import mimetypes
from pathlib import Path


def data_url(image_path: Path) -> str:
    if not image_path.is_file():
        raise SystemExit(f"Image not found: {image_path}")
    media_type = mimetypes.guess_type(image_path.name)[0] or "application/octet-stream"
    if not media_type.startswith("image/"):
        raise SystemExit(f"Unsupported image type: {image_path}")
    payload = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{media_type};base64,{payload}"


parser = argparse.ArgumentParser(description="Build a self-contained visual comparison board.")
parser.add_argument("--reference", required=True, type=Path)
parser.add_argument("--render", required=True, type=Path)
parser.add_argument("--output", required=True, type=Path)
parser.add_argument("--title", default="3D reference comparison")
parser.add_argument("--force", action="store_true")
args = parser.parse_args()

output = args.output.resolve()
if output.exists() and not args.force:
    raise SystemExit(f"Refusing to overwrite {output}; pass --force after reviewing the existing file.")

reference_url = data_url(args.reference.resolve())
render_url = data_url(args.render.resolve())
title = html.escape(args.title)
reference_json = json.dumps(reference_url)
render_json = json.dumps(render_url)

document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>
:root {{ color-scheme: dark; font-family: ui-sans-serif, system-ui, sans-serif; background:#111; color:#f4f1e8; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; padding:24px; }}
main {{ max-width:1200px; margin:auto; }}
h1 {{ font-size:clamp(1.5rem,3vw,2.5rem); margin:0 0 8px; }}
.note {{ color:#aaa; margin:0 0 20px; }}
.compare {{ position:relative; aspect-ratio:16/10; overflow:hidden; border:1px solid #3b3b37; background:#222; }}
.compare img {{ position:absolute; inset:0; width:100%; height:100%; object-fit:contain; background:#222; }}
#render-wrap {{ position:absolute; inset:0; overflow:hidden; width:50%; border-right:1px solid #fff; }}
#render-wrap img {{ width:100vw; max-width:1200px; }}
#slider {{ width:100%; margin:16px 0 24px; }}
.grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; }}
.panel {{ border:1px solid #3b3b37; background:#191918; padding:12px; min-height:120px; }}
.panel h2 {{ font-size:.82rem; text-transform:uppercase; letter-spacing:.08em; color:#aaa; margin:0 0 10px; }}
canvas {{ width:100%; height:auto; image-rendering:auto; }}
#metrics {{ font-variant-numeric:tabular-nums; white-space:pre-wrap; }}
@media (max-width:760px) {{ body {{ padding:12px; }} .grid {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
<main>
<h1>{title}</h1>
<p class="note">Align framing and lighting before interpreting the pixel metric. Judge silhouette and proportions first.</p>
<section class="compare" id="compare" aria-label="Overlay comparison">
  <img id="reference" alt="Reference image">
  <div id="render-wrap"><img id="render" alt="Rendered reconstruction"></div>
</section>
<label for="slider">Rendered image coverage</label>
<input id="slider" type="range" min="0" max="100" value="50">
<section class="grid">
  <article class="panel"><h2>Difference map</h2><canvas id="difference" width="640" height="400"></canvas></article>
  <article class="panel"><h2>Measured signal</h2><div id="metrics">Loading images…</div></article>
  <article class="panel"><h2>Review order</h2><ol><li>Silhouette</li><li>Proportions</li><li>Placement and camera</li><li>Large value groups</li><li>Materials</li><li>Distinctive details</li></ol></article>
</section>
</main>
<script>
const referenceSource = {reference_json};
const renderSource = {render_json};
const reference = document.querySelector('#reference');
const render = document.querySelector('#render');
const slider = document.querySelector('#slider');
const renderWrap = document.querySelector('#render-wrap');
slider.addEventListener('input', () => renderWrap.style.width = `${{slider.value}}%`);

function drawContained(ctx, image, width, height) {{
  ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, width, height);
  const scale = Math.min(width / image.naturalWidth, height / image.naturalHeight);
  const w = image.naturalWidth * scale, h = image.naturalHeight * scale;
  ctx.drawImage(image, (width - w) / 2, (height - h) / 2, w, h);
}}

async function compare() {{
  await Promise.all([reference.decode(), render.decode()]);
  const canvas = document.querySelector('#difference');
  const width = canvas.width, height = canvas.height;
  const a = document.createElement('canvas'), b = document.createElement('canvas');
  a.width = b.width = width; a.height = b.height = height;
  drawContained(a.getContext('2d', {{willReadFrequently:true}}), reference, width, height);
  drawContained(b.getContext('2d', {{willReadFrequently:true}}), render, width, height);
  const ad = a.getContext('2d').getImageData(0, 0, width, height).data;
  const bd = b.getContext('2d').getImageData(0, 0, width, height).data;
  const out = canvas.getContext('2d').createImageData(width, height);
  let total = 0, changed = 0;
  for (let i = 0; i < ad.length; i += 4) {{
    const dr = Math.abs(ad[i] - bd[i]), dg = Math.abs(ad[i+1] - bd[i+1]), db = Math.abs(ad[i+2] - bd[i+2]);
    const delta = (dr + dg + db) / 3;
    total += delta; if (delta > 24) changed++;
    out.data[i] = Math.min(255, delta * 3); out.data[i+1] = Math.min(255, delta * .35); out.data[i+2] = Math.min(255, delta * .1); out.data[i+3] = 255;
  }}
  canvas.getContext('2d').putImageData(out, 0, 0);
  const mae = total / (width * height);
  const changedPercent = changed / (width * height) * 100;
  document.querySelector('#metrics').textContent = `Normalized canvas: ${{width}} × ${{height}}\nMean absolute RGB delta: ${{mae.toFixed(2)}} / 255\nPixels above delta 24: ${{changedPercent.toFixed(2)}}%\n\nThis is a framing-sensitive signal, not a likeness score.`;
}}
reference.src = referenceSource; render.src = renderSource;
compare().catch((error) => document.querySelector('#metrics').textContent = `Comparison failed: ${{error.message}}`);
</script>
</body>
</html>
"""

output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(document, encoding="utf-8")
print(f"Generated {output}")
