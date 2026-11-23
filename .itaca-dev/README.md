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
