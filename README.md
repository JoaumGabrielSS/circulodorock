# Círculo do Rock, 8ª Edição

Site oficial do evento Círculo do Rock, 8ª edição, realizado em Planaltina/DF.

## Estrutura

```text
.
├── index.html
├── assets
│   ├── css
│   │   └── styles.css
│   ├── images
│   │   ├── bandas
│   │   │   ├── a-drink-to-death
│   │   │   ├── asgard
│   │   │   ├── ghon
│   │   │   ├── mitsein.jpg
│   │   │   ├── naught-dog
│   │   │   ├── o-dia-d
│   │   │   └── walk-again
│   │   ├── organizacao
│   │   ├── comunicado-circulo-do-rock.jpg
│   │   ├── logo-rock-na-pedra.jpg
│   │   └── qrcode-sympla.png
│   ├── js
│   │   └── main.js
│   └── video
│       └── anuncio-oficial.mp4
├── scripts
│   └── validate.py
├── CNAME
├── robots.txt
└── sitemap.xml
```

## Ingressos

A emissão de ingressos é feita externamente pelo Sympla:

`https://www.sympla.com.br/evento/circulo-do-rock-8-ediCAo/3522896`

O site não processa cadastro, pagamento ou dados pessoais. Portanto, não precisa de backend para essa integração.

## Bandas confirmadas

1. O Dia D
2. Mitsein
3. A Drink to Death
4. Naught Dog
5. GhoN
6. Walk Again
7. Asgard

Cada card utiliza uma foto principal e links oficiais para Instagram e Spotify.

## Teste local

```bash
python3 -m http.server 8080
```

Acesse `http://localhost:8080`.

## Validação

```bash
python3 scripts/validate.py
git diff --check
```

## Atualização de bandas

1. Crie uma pasta em `assets/images/bandas/nome-da-banda/`.
2. Salve uma foto principal otimizada em WebP.
3. Duplique um `article.band-card` na seção `#bandas`.
4. Atualize nome, texto, imagem, Instagram e Spotify.
5. Informe `width`, `height`, `loading="lazy"` e `decoding="async"`.
6. Teste localmente antes do commit.

## Pendências de conteúdo

Adicionar quando forem confirmados:

1. Data do evento
2. Horário de início e encerramento
3. Endereço completo
4. Link para mapa
5. Classificação indicativa
6. Programação e ordem das bandas
7. Imagem social em formato 1200 x 630
8. Legenda do vídeo em `assets/captions/`
