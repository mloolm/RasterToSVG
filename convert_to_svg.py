import os
import subprocess
from pathlib import Path

# 📁 Папки
input_folder = Path("input_images")
output_folder = Path("output_svg")
svg_folder = output_folder / "result"

output_folder.mkdir(exist_ok=True)
svg_folder.mkdir(parents=True, exist_ok=True)

# 🧾 HTML-заготовка
html_lines = [
    "<!DOCTYPE html>",
    "<html lang='ru'>",
    "<head><meta charset='UTF-8'><title>SVG просмотр</title><style>",
    "body{font-family:sans-serif;padding:2rem;background:#f0f0f0}",
    ".item{margin-bottom:2rem;padding:1rem;background:#fff;border-radius:8px;box-shadow:0 0 4px rgba(0,0,0,0.1)}",
    ".images{display:flex;gap:2rem;align-items:center}",
    "img,object{border:1px solid #ccc;max-width:45%}",
    "</style></head><body><h1>Оригиналы и SVG</h1>"
]

# 🔁 Обработка изображений
for file in input_folder.glob("*.[pjP][pnN]*g"):
    stem = file.stem
    pbm_path = svg_folder / f"{stem}.pbm"
    svg_path = svg_folder / f"{stem}.svg"
    copied_input = output_folder / file.name

    print(f"🔄 Обработка: {file.name}")

    # Копируем оригинал рядом
    if not copied_input.exists():
        copied_input.write_bytes(file.read_bytes())

    # PNG/JPG → PBM
    subprocess.run([
        "convert", str(file),
        "-threshold", "50%",
        "-compress", "none",
        str(pbm_path)
    ], check=True)

    # PBM → SVG
    subprocess.run([
        "potrace", str(pbm_path),
        "-s", "-o", str(svg_path)
    ], check=True)

    # 🧹 Удаляем PBM
    pbm_path.unlink(missing_ok=True)

    # Добавляем в HTML
    html_lines.append(f"""
    <div class="item">
        <div class="images">
            <div><div><b>{file.name}</b></div><img src="{file.name}"></div>
            <div><div><b>{svg_path.relative_to(output_folder)}</b></div><object type="image/svg+xml" data="{svg_path.relative_to(output_folder)}"></object></div>
        </div>
    </div>
    """)

# 📄 Финализируем HTML
html_lines.append("</body></html>")
html_path = output_folder / "index.html"
html_path.write_text("\n".join(html_lines), encoding="utf-8")

print(f"\n✅ Готово! Открой файл {html_path.resolve()} в браузере.")
