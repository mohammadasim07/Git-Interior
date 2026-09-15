import os

cols = 46
rows = 7
cell_w = 11
cell_h = 11
gap = 4
start_x = 50
start_y = 55

waypoints = [
    (0, 1),
    (2, 1),   # eat 1
    (7, 1),
    (7, 3),   # eat 2
    (11, 3),  # eat 3
    (11, 5),  # eat 4
    (15, 5),
    (15, 2),  # eat 5
    (20, 2),  # eat 6
    (24, 2),
    (24, 4),  # eat 7
    (28, 4),  # eat 8
    (32, 4),
    (32, 1),  # eat 9
    (37, 1),  # eat 10
    (37, 4),
    (41, 4),  # eat 11
    (41, 1),  # eat 12
    (43, 1),  # eat 13
    (43, 3),  # eat 14
    (44, 3),  # eat 15
    (44, 5),  # eat 16
    (42, 5),  # eat 17
    (42, 6),  # eat 18
    (44, 6),  # eat 19
    (45, 6),
    (45, 0),
    (0, 0),
    (0, 1)
]

dists = []
total_dist = 0
for i in range(len(waypoints)-1):
    dx = abs(waypoints[i+1][0] - waypoints[i][0])
    dy = abs(waypoints[i+1][1] - waypoints[i][1])
    d = dx + dy
    dists.append(d)
    total_dist += d

keyframe_steps = []
cum = 0
cum_list = [0]
for d in dists:
    cum += d
    cum_list.append(cum)

for i, p in enumerate(waypoints):
    pct = (cum_list[i] / total_dist) * 100
    px = start_x + p[0] * (cell_w + gap)
    py = start_y + p[1] * (cell_h + gap)
    keyframe_steps.append((pct, px, py))

eaten_indices = [1, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24]
eaten_dict = {}
for idx in eaten_indices:
    c, r = waypoints[idx]
    pct = keyframe_steps[idx][0]
    eaten_dict[(c, r)] = pct

css_lines = []
css_lines.append("@keyframes snakeMove {\n")
for pct, px, py in keyframe_steps:
    css_lines.append(f"  {pct:.2f}% {{ transform: translate({px}px, {py}px); }}\n")
css_lines.append("}\n")

# Commit eating animations
for (c, r), pct in eaten_dict.items():
    anim_name = f"eat_{c}_{r}"
    p_before = max(0.0, pct - 0.25)
    p_hit = pct
    p_eaten = min(95.0, pct + 0.6)
    css_lines.append(f"@keyframes {anim_name} {{\n")
    css_lines.append(f"  0%, {p_before:.2f}% {{ fill: #39d353; }}\n")
    css_lines.append(f"  {p_hit:.2f}% {{ fill: #ffffff; filter: drop-shadow(0 0 6px #ffffff); }}\n")
    css_lines.append(f"  {p_eaten:.2f}%, 96.0% {{ fill: #161b22; filter: none; }}\n")
    css_lines.append(f"  98.0%, 100.0% {{ fill: #39d353; }}\n")
    css_lines.append("}\n")

css_lines.append("""
  .bg { fill: #0b0f19; stroke: #1e293b; stroke-width: 1; rx: 12; }
  .grid-cell { rx: 2.5; width: 11px; height: 11px; }
  .empty-cell { fill: #161b22; }
  .snake-seg {
    position: absolute;
    width: 11px;
    height: 11px;
    rx: 3;
    animation: snakeMove 14s linear infinite;
  }
  .snake-h  { fill: #38bdf8; filter: drop-shadow(0 0 6px #38bdf8); }
  .snake-s1 { fill: #34d399; animation-delay: -0.12s; }
  .snake-s2 { fill: #10b981; animation-delay: -0.24s; }
  .snake-s3 { fill: #059669; animation-delay: -0.36s; }
  .snake-s4 { fill: #047857; animation-delay: -0.48s; }
""")

cells_svg = []
for c in range(cols):
    for r in range(rows):
        x = start_x + c * (cell_w + gap)
        y = start_y + r * (cell_h + gap)
        if (c, r) in eaten_dict:
            cells_svg.append(f'    <rect x="{x}" y="{y}" class="grid-cell" style="animation: eat_{c}_{r} 14s linear infinite; fill: #39d353;" />\n')
        else:
            if (c, r) in [(4, 2), (9, 4), (16, 6), (22, 1), (30, 0), (35, 6), (42, 0), (43, 0), (44, 1)]:
                cells_svg.append(f'    <rect x="{x}" y="{y}" class="grid-cell" fill="#006d32" />\n')
            elif (c, r) in [(42, 2), (43, 2), (44, 4), (43, 6)]:
                cells_svg.append(f'    <rect x="{x}" y="{y}" class="grid-cell" fill="#26a641" />\n')
            else:
                cells_svg.append(f'    <rect x="{x}" y="{y}" class="grid-cell empty-cell" />\n')

svg_content = f"""<svg fill="none" viewBox="0 0 800 185" width="100%" height="185" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
{''.join(css_lines)}
    </style>
  </defs>

  <!-- Container Box -->
  <rect width="800" height="185" class="bg" />

  <!-- Telemetry Header -->
  <g transform="translate(30, 26)">
    <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12.5" font-weight="600" fill="#94a3b8">CONTRIBUTION ACTIVITY &amp; COMMIT EATING GAME</text>
    <text x="740" y="0" font-family="Consolas, monospace" font-size="11.5" font-weight="600" fill="#38bdf8" text-anchor="end">133+ Commits · Snake Eating Commits 🐍</text>
  </g>

  <!-- Month Labels -->
  <g transform="translate(50, 46)" fill="#64748b" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9">
    <text x="0">Oct</text><text x="60">Nov</text><text x="120">Dec</text><text x="180">Jan</text><text x="240">Feb</text><text x="300">Mar</text><text x="360">Apr</text><text x="420">May</text><text x="480">Jun</text><text x="540">Jul</text><text x="600">Aug</text><text x="660">Sep</text>
  </g>

  <!-- Grid of Commits -->
  <g id="grid">
{''.join(cells_svg)}
  </g>

  <!-- Active Snake Eating Commits -->
  <rect class="snake-seg snake-s4" x="0" y="0" />
  <rect class="snake-seg snake-s3" x="0" y="0" />
  <rect class="snake-seg snake-s2" x="0" y="0" />
  <rect class="snake-seg snake-s1" x="0" y="0" />
  <rect class="snake-seg snake-h"  x="0" y="0" />

  <!-- Legend -->
  <g transform="translate(670, 168)">
    <text x="-30" y="8" font-family="sans-serif" font-size="8.5" fill="#64748b">Less</text>
    <rect x="-6" y="0" width="9" height="9" rx="2" fill="#161b22" />
    <rect x="6" y="0" width="9" height="9" rx="2" fill="#0e4429" />
    <rect x="18" y="0" width="9" height="9" rx="2" fill="#006d32" />
    <rect x="30" y="0" width="9" height="9" rx="2" fill="#26a641" />
    <rect x="42" y="0" width="9" height="9" rx="2" fill="#39d353" />
    <text x="56" y="8" font-family="sans-serif" font-size="8.5" fill="#64748b">More</text>
  </g>
</svg>"""

with open(r"d:\Git-Interior\assets\contribution-snake.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

with open(r"d:\Git-Interior\mohammadasim07\assets\contribution-snake.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("SUCCESS: Generated synchronized snake eating commits SVG!")
