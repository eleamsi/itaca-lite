# .itaca-dev

Strumenti per sviluppare Itaca Lite. Non servono per usarla: l'app è solo `Itaca Lite.html`.

## changelog/

Note della finestra «Novità». La fonte è il blocco
`<script type="application/json" id="itacaChangelog">` dentro `Itaca Lite.html`.

- `X.Y.Z.md` = testo della Release su GitHub senza «Come aggiornare»
- `dates.txt` = una riga «X.Y.Z AAAA-MM-GG» per versione

```
python3 build.py estrai      # ricrea X.Y.Z.md e dates.txt dall'HTML
python3 build.py             # rimette nell'HTML le note nuove o cambiate
python3 build.py controlla   # riscrivere deve lasciare l'HTML identico byte per byte
```

Prima del commit di una versione: scrivere `X.Y.Z.md`, aggiungere la data in `dates.txt`, lanciare `build.py`.

## critters/

Animazioni in pixel art (Loki, barchetta, slitta). Si versionano solo i sorgenti:
i PNG, `sprites.json`, `out.css`, `out.html` e `preview.html` vengono rigenerati.

```
python3 gen.py     # fotogrammi (griglie ASCII) → PNG + sprites.json
python3 build.py   # → out.css, out.html, preview.html (?m=cat|boat|sleigh)
```

Dopo una modifica bisogna ricopiare `out.css`, `out.html` e `critters.js` in `Itaca Lite.html`.
`scene.py` crea una scena ingrandita per controllare la linea di galleggiamento.

## itaca-icon.svg / itaca-icon.png

Icona di Finder per `Itaca Lite.html` (interno bianco, tratti neri, sfondo trasparente).
Il PNG 1024 px si ottiene dall'SVG con Chrome headless (`--default-background-color=00000000 --screenshot`).

## File di prova

- `prova.docx`, `rotto.docx`: documenti Word incorporati (valido e rovinato)
- `testo/`: file di testo incorporati (txt, csv, json, html, svg, codice, un log da 5000 righe, un file vuoto)

## .gitignore

Esclude i file di sistema (`.DS_Store`, `Thumbs.db`) e i file generati delle animazioni,
così le regole valgono uguali su ogni PC.
