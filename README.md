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
│   │   │   └── mitsein.jpg
│   │   ├── comunicado-circulo-do-rock.jpg
│   │   ├── logo-rock-na-pedra.jpg
│   │   └── qrcode-sympla.png
│   ├── js
│   │   └── main.js
│   ├── video
│   │   └── anuncio-oficial.mp4
│   └── captions
├── CNAME
├── robots.txt
└── sitemap.xml
```

## Ingressos

A emissão de ingressos é feita externamente pelo Sympla:

`https://www.sympla.com.br/evento/circulo-do-rock-8-ediCAo/3522896`

O site não processa cadastro, pagamento ou dados pessoais. Por isso, não precisa de backend para essa integração.

## Teste local

```bash
python3 -m http.server 8080
```

Acesse `http://localhost:8080`.

## Atualização de bandas

1. Salve a imagem em `assets/images/bandas/`.
2. Edite a seção `#bandas` no `index.html`.
3. Informe `width`, `height`, `loading="lazy"` e `decoding="async"` na imagem.
4. Teste localmente antes do commit.

## Pendências de conteúdo

Adicionar ao site quando forem confirmados:

1. Data do evento
2. Horário de início e encerramento
3. Endereço completo
4. Link para mapa
5. Classificação indicativa
6. Programação e ordem das bandas
7. Imagem social em formato 1200 x 630
8. Legenda do vídeo em `assets/captions/`
