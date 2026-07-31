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
    "O Dia D",
    "Mitsein",
    "A Drink to Death",
    "Naught Dog",
    "GhoN",
    "Walk Again",
    "Asgard",
    "instagram.com/banda_odiad_hc",
    "instagram.com/mitseinofficial",
    "instagram.com/adrinktodeath",
    "instagram.com/naughty.dog1",
    "instagram.com/bandaghon",
    "instagram.com/_walkagain_",
    "instagram.com/asgarddf",
]
for item in required:
    if item not in html:
        errors.append(f"Conteúdo obrigatório ausente: {item}")

card_count = html.count('<article class="band-card">')
if card_count != 7:
    errors.append(f"Quantidade de cards de banda inválida: {card_count}. Esperado: 7")

spotify_count = html.count('band-link band-link-spotify')
instagram_count = html.count('band-link band-link-instagram')
if spotify_count != 7:
    errors.append(f"Quantidade de links do Spotify inválida: {spotify_count}. Esperado: 7")
if instagram_count != 7:
    errors.append(f"Quantidade de links do Instagram inválida: {instagram_count}. Esperado: 7")

if errors:
    print("VALIDAÇÃO FALHOU")
    for error in errors:
        print(f"  ERRO: {error}")
    sys.exit(1)

print("VALIDAÇÃO OK")
print(f"  index.html: {html_path.stat().st_size / 1024:.1f} KiB")
print("  Bandas confirmadas: 7")
print("  Links do Spotify: 7")
print("  Links do Instagram: 7")
print("  Base64 no HTML: 0")
print("  Link do Sympla: presente")
print("  Arquivos locais referenciados: presentes")
