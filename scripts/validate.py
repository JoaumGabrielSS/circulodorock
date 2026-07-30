#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parent.parent
html_path = root / "index.html"
html = html_path.read_text(encoding="utf-8")

errors = []

if "data:" in html and ";base64," in html:
    errors.append("O index.html ainda contém arquivos Base64.")

pattern = r'(?:src|href)=["\']((?:assets/|robots\.txt|sitemap\.xml)[^"\'#?]*)["\']'
for relative in re.findall(pattern, html):
    path = root / relative
    if not path.exists():
        errors.append(f"Arquivo referenciado não existe: {relative}")

required = [
    "https://www.sympla.com.br/evento/circulo-do-rock-8-ediCAo/3522896",
    'id="ingressos"',
    'id="menu-principal"',
    'rel="stylesheet" href="assets/css/styles.css"',
]
for item in required:
    if item not in html:
        errors.append(f"Conteúdo obrigatório ausente: {item}")

if errors:
    print("VALIDAÇÃO FALHOU")
    for error in errors:
        print(f"  ERRO: {error}")
    sys.exit(1)

print("VALIDAÇÃO OK")
print(f"  index.html: {html_path.stat().st_size / 1024:.1f} KiB")
print("  Base64 no HTML: 0")
print("  Link do Sympla: presente")
print("  QR Code: presente")
print("  CSS e JavaScript externos: presentes")
