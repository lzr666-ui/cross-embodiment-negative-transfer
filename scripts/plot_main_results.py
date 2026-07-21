import csv

rows = []
with open("paper_assets/tables/main_results.csv", "r") as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append({
            "setting": r["setting"],
            "loss": float(r["target_val_loss"]),
        })

width = 900
height = 520
margin_left = 90
margin_bottom = 130
margin_top = 50
plot_height = height - margin_top - margin_bottom
bar_width = 70
gap = 45

max_loss = max(r["loss"] for r in rows) * 1.15

def y(loss):
    return margin_top + plot_height * (1 - loss / max_loss)

svg = []
svg.append(f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">')
svg.append('<rect width="100%" height="100%" fill="white"/>')
svg.append('<text x="450" y="30" text-anchor="middle" font-size="20" font-family="Arial" font-weight="bold">Target-Domain Validation Loss on Franka</text>')

# axis
svg.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="black"/>')
svg.append(f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-30}" y2="{height-margin_bottom}" stroke="black"/>')

colors = ["#4C78A8", "#59A14F", "#F28E2B", "#E15759", "#B07AA1", "#9C755F"]

for i, r in enumerate(rows):
    x = margin_left + 30 + i * (bar_width + gap)
    bar_y = y(r["loss"])
    bar_h = height - margin_bottom - bar_y
    color = colors[i % len(colors)]

    svg.append(f'<rect x="{x}" y="{bar_y}" width="{bar_width}" height="{bar_h}" fill="{color}"/>')
    svg.append(f'<text x="{x + bar_width/2}" y="{bar_y - 8}" text-anchor="middle" font-size="12" font-family="Arial">{r["loss"]:.3f}</text>')

    label = r["setting"]
    svg.append(f'<text x="{x + bar_width/2}" y="{height-margin_bottom+20}" text-anchor="end" font-size="11" font-family="Arial" transform="rotate(-35 {x + bar_width/2},{height-margin_bottom+20})">{label}</text>')

# y label
svg.append(f'<text x="20" y="{margin_top + plot_height/2}" text-anchor="middle" font-size="14" font-family="Arial" transform="rotate(-90 20,{margin_top + plot_height/2})">Target-val loss</text>')

svg.append('</svg>')

with open("paper_assets/figures/main_results.svg", "w") as f:
    f.write("\\n".join(svg))

print("Saved to paper_assets/figures/main_results.svg")
