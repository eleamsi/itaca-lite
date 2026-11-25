# Estetica di Erevs26 nella 2.0.0: piano di integrazione

Fonte: issue #33 e repo `Erevs26/itaca-lite-estetica` (file `INTEGRAZIONE-ESTETICA.md`, preparato su Itaca **1.13.0**).
Ramo: `release-2.0.0`. Questo file serve da traccia: si spunta man mano.

## 1. Cosa propone Erevs26 (in breve)

**Lotto 1, logo.**
- La colonna greca diventa una galea in stile cartone, con sole, isola e onde, senza cerchio.
- Intestazione grande: logo da 112 × 73 px, «Itaca» a 32 px e sotto «LITE» con la versione.
- La barca ondeggia sempre e il mare scorre. Quando si cambia documento arriva una folata: la vela si gonfia, la barca dà uno strappo e le onde accelerano per circa 2,5 s.
- Interruttore «Logo animato», salvato nella chiave localStorage `itaca-logo-motion`.
- Favicon e icone scaricabili (PNG e ICO) con la galea.
- Colori fissi oliva e sabbia, con una variante «Notte di luna» per il tema scuro.

**Lotto 2, pagina di benvenuto.**
- Pagina a tutto schermo con la scena grande, stelle di notte e nuvole di giorno.
- Testi: «Benvenuto su Itaca», la frase e i pulsanti Riprendi il viaggio / Apri cartella / Importa cartella.
- Ogni 7 s arriva una folata.
- Clic ovunque = la scena vola sul logo dell'intestazione. Esc = si entra subito.
- Compare una volta per scheda (sessionStorage). Scelta Nessuna / Benvenuto nella chiave localStorage `itaca-welcome`.

Sono blocchi «autonomi» incollati in fondo al file. Non chiamano il codice dell'app: lo osservano dall'esterno.

## 2. Problemi con la 2.0.0 attuale

| # | Problema | Perché | Cosa fare |
|---|---|---|---|
| P1 | Le impostazioni del logo smettono di funzionare | Dalla 1.15 esistono Dimensione (`brandSize`), Ingrandisci (`brandTarget`) e Versione (`versionPlacement`): il nuovo CSS fissa 112 px e 32 px e le ignora | Integrare: misure di base × `--logo-scale`/`--title-scale`, versione «accanto» = nella riga LITE, «sotto»/«in basso»/«nascosta» come oggi |
| P2 | Cambio documento riconosciuto da `document.title` | Dalla 1.39 il titolo può essere il titolo del documento, cambia rinominandolo, e la stampa PDF lo cambia per il nome del file → folate false | Chiamare la folata da `onDocumentShown()` (solo quando cambia `current`) |
| P3 | Impostazioni fuori da `settings` | Chiavi proprie non in `resettableKeys`: Ripristina non le tocca e la ricerca non conosce i loro sinonimi | `settings.logoMotion` e `settings.welcomePage` in `settingChoices`/`defaultSettings` |
| P4 | La pagina di benvenuto finisce sotto altre finestre | È un `div` con z-index 9000, ma l'avviso aggiornamento, l'avviso Novità, i toast e i dialog (bozza da ripristinare, cartella che non risponde) stanno nel *top layer* e le passano sopra | Mostrarla come `<dialog>` modale (o rimandare quegli avvisi a dopo la chiusura) |
| P5 | Doppia richiesta della cartella | `reopenOnFirstInteraction` chiede l'accesso al primo pointerdown ovunque. Il trucco di Erevs (stopImmediatePropagation) funziona solo se il suo listener è registrato prima, e dipende dai tempi | Escludere `#welcome` in `reopen()`. I pulsanti chiamano direttamente `chooseFolder(true)`, `chooseFolder()` e `pickImportedFolder()` |
| P6 | «Riprendi il viaggio» capito leggendo i testi dei pulsanti | Regex su «consenti / mostra documenti»: si rompe se cambia una parola | Usare lo stato vero: `folderAccessPending`, `hasWorkspaceFolder()`, `root?.name` |
| P7 | Focus e tastiera | Il `div role=dialog` non blocca il Tab: si finisce nell'app che sta dietro | Con `<dialog>` modale si risolve |
| P8 | Caratteri Windows fissi | 'Segoe UI' e 'Sitka' scritti nel CSS: sul Mac si va al ripiego | Usare `var(--sans)`, `var(--read)`, `var(--display)` |
| P9 | Quattro copie dello stesso disegno | Intestazione, benvenuto, `itacaIconSvg` e favicon ripetono gli stessi tracciati: ogni ritocco va fatto 4 volte | Una sola fonte (`<template id="itacaArt">`) clonata da JS, con i colori come variabili |
| P10 | Favicon a 16 px illeggibile | È il disegno intero senza onde | Versione davvero semplificata (vela + scafo, tratti spessi) |
| P11 | Tavolozze | Il logo ha colori fissi oliva e sabbia, l'app ne ha 11 (Laguna è blu). La regola Natale su `.brandmark .brand-fill` non vale più | Vedi decisione D1 |
| P12 | Costo dell'animazione continua | Chrome non compone le trasformazioni degli elementi *dentro* un SVG: ogni fotogramma ridipinge l'intestazione, sempre, anche mentre si scrive | Fermarla a finestra non attiva o nascosta. Misurare: se pesa, separare in strati (mare / barca) come elementi HTML composti |
| P13 | Spazio verticale | L'intestazione passa da 60 a 96 px: meno righe di file visibili, soprattutto su portatili piccoli | Dimensione «Compatta» (vedi P1) |
| P14 | Icona di Finder | Oggi è la colonna bianca e nera (scelta dell'utente) | Rifare `.itaca-dev/itaca-icon.svg`/`.png` con la galea, se confermato (D2) |

## 3. Il volo barca → logo (quello che non va)

Cause trovate nel codice di Erevs:

1. **Logo doppio.** Durante il volo lo sfondo della pagina sfuma da 0,35 s a 1,05 s, ma il logo dell'intestazione non viene mai nascosto. Si vede già al suo posto mentre la barca sta ancora arrivando, poi i due si sovrappongono per un'ultima dissolvenza di 0,25 s. Le due barche sono anche in fasi diverse dell'ondeggiamento: per esempio `.wl-w1` non ha il ritardo −1,2 s che ha `.lg-w1`.
2. **Scatti.** La trasformazione è applicata a `.wl-stage`, che contiene anche il mare `::before`, grande 300 vw × 200 vh. Si scala quindi un livello enorme.
3. **Animazioni interne durante il volo.** Ondeggiamento e onde girano mentre lo SVG cambia scala, quindi il browser ridisegna i tracciati a ogni fotogramma invece di spostare un'immagine già pronta.
4. **Movimento meccanico.** Una sola transizione `transform` in linea retta, avviata con una classe e chiusa con `setTimeout` (1150 ms e 1450 ms) che non sono legati alla fine reale dell'animazione.

Soluzione (FLIP con Web Animations):
- All'avvio del volo, `html.welcome-landing` nasconde il logo dell'intestazione (`visibility: hidden`). Così c'è un solo logo in ogni momento.
- Le animazioni interne della scena vengono messe in pausa. Quelle del logo dell'intestazione si portano allo stesso `currentTime` e restano in pausa: le due barche coincidono pixel per pixel.
- Il mare e il cielo diventano livelli propri dell'overlay, non figli dello stage: si sfuma solo l'opacità.
- Il volo è `stage.animate()` con `transform` e `will-change: transform`, quindi tutto sul compositore. Il percorso è leggermente ad arco: X e Y su due elementi annidati con curve diverse. Durata circa 900 ms.
- A `animation.finished`, nello stesso fotogramma: si mostra il logo vero, si toglie la pagina e le animazioni del logo ripartono. Niente dissolvenza tra i due.
- Riduci movimento, logo non visibile o barra chiusa: dissolvenza breve come oggi.

## 4. Miglioramenti utili (oltre all'estetica)

- **Benvenuto che serve a qualcosa.** «Riprendi» riapre la cartella ricordata e il documento lasciato. Sotto ci sono le **cartelle salvate** come scelte rapide e, se esistono, **Le mie bozze**. Invio = Riprendi.
- **Novità e aggiornamenti nella pagina.** Se c'è una versione nuova o non ancora vista, una riga «Novità della X.Y» o «Aggiornamento disponibile» nella pagina, al posto dei due avvisi che oggi le comparirebbero sopra (P4).
- **Copre il caricamento.** La cartella si riapre dietro la pagina, quindi entrando l'app è già pronta.
- **Folata solo quando serve.** Al cambio documento, non quando si torna alla stessa scheda o si aggiorna il disco.
- **Pagina iniziale** in Impostazioni › Documenti › Apertura (è lì che si cerca «all'avvio»). «Logo animato» va in Aspetto › Logo, vicino a Dimensione.

## 5. Decisioni da chiedere all'utente

- **D1 Colori del logo:** originali di Erevs (oliva/sabbia, «Notte di luna» al buio) con qualunque tavolozza *(consigliato: è un'illustrazione, come l'icona di un'app)* oppure tinte derivate dalla tavolozza attiva.
- **D2 Icona scaricabile e di Finder:** galea a colori *(consigliato)* oppure resta la colonna.
- **D3 Dimensione predefinita dell'intestazione:** quella grande di Erevs *(consigliato, è il senso del restyling)*, con «Compatta» per chi vuole spazio.

## 6. Ordine di lavoro

- [ ] **Fase 1 — Logo**
  - [ ] Fonte unica: `<template id="itacaArt">` + variabili `--lg-*` (chiaro/scuro).
  - [ ] Intestazione con le dimensioni Compatta/Normale/Grande, `brandTarget` e `versionPlacement` (P1, P13).
  - [ ] `settings.logoMotion` (Aspetto › Logo) + riduci movimento + pausa a finestra inattiva (P3, P12).
  - [ ] Folata da `onDocumentShown` (P2), mare che accelera con WAAPI.
  - [ ] Favicon semplificata (P10), `itacaIconSvg` dalla fonte unica (P9), icona di Finder (P14).
  - [ ] Togliere le regole vecchie `.brand-line`/`.brand-fill` e quella di Natale.
  - [ ] Misurare il costo dell'animazione continua (Performance del browser).
- [ ] **Fase 2 — Pagina di benvenuto**
  - [ ] `<dialog id="welcome">` modale, caratteri dell'app, `settings.welcomePage` in Documenti › Apertura (P3, P4, P7, P8).
  - [ ] Azioni con le funzioni interne, `#welcome` escluso da `reopen()` (P5, P6).
  - [ ] Cartelle salvate, bozze, Novità/aggiornamento nella pagina; avvisi rimandati finché è aperta.
  - [ ] Cielo/stelle/nuvole come da proposta; mare fuori dallo stage.
- [ ] **Fase 3 — Volo** (sezione 3).
- [x] **Fase 4 — Verifica**
  - [x] Temi chiaro e scuro, tutte le tavolozze, Natale.
  - [x] Barra a destra, barra chiusa, finestra stretta, riduci movimento.
  - [x] Ripristina, ricerca nelle Impostazioni.
  - [ ] Da file:// con una cartella ricordata (un solo prompt): da provare dall'utente.
  - [ ] Changelog 2.0.0 e chiusura di #33 con la milestone: al rilascio.

## 7. Stato

**Fase 1 fatta (25/11/2026).** Indicazioni dell'utente:
- folate **a caso** (ogni 25–70 s), non al cambio documento;
- solo caratteri già presenti in Itaca (`--serif`, `--sans`);
- pagina di benvenuto pulita, bella e utile: nessun avviso o finestra che le si sovrapponga.

Come è fatta:
- **Disegno unico.** `#itacaLogo` nella testata è l'unica copia. `itacaArtSvg()` la clona per la favicon (solo la nave, segue chiaro/scuro del sistema) e per le icone PNG e ICO. I colori stanno solo nelle due regole `.itaca-logo`. Parti marcate: `lg-detail` (tolte nella favicon), `lg-oars`.
- **Impostazioni › Aspetto › Logo.**
  - Dimensione Compatta / Normale / Grande; «Più grande» diventa Grande.
  - Vale per.
  - Versione Sotto il nome / In basso / Nascosta; «accanto» diventa «sotto».
  - Logo animato (`settings.logoMotion`).
- **Movimento.** È fermo con «riduci movimento» del sistema e va in pausa quando Itaca non è in primo piano. Costo misurato: circa +1,4 % di CPU con Chrome.
- **Testata.** È un contenitore (`cqw`), quindi a 220 px logo e nome si riducono senza uscire.

Prossimo: Fase 2 (pagina di benvenuto). Per il benvenuto la scena si potrà clonare da `#itacaLogo`.

**Fase 2 fatta (25/11/2026).**
- **Struttura.** `<dialog id="welcome">` modale a tutto schermo, nel livello superiore: blocca Tab e scorciatoie. La scena è un clone di `#itacaLogo`, quindi c'è un solo disegno con le stesse animazioni. Cielo (nuvole di giorno, stelle di notte) e mare sono livelli propri, separati dalla scena; l'orizzonte è calcolato dalla base dell'isola.
- **Pulsante principale.** «Riprendi il viaggio · Ultima rotta: cartella · documento» riapre la cartella, chiedendo il permesso con quel clic. Senza cartella ricordata diventa «Scegli la cartella» (consigliata quella di Itaca), oppure «Importa una cartella» senza File System Access. In più «Un'altra cartella…».
- **Scelte rapide.** «Rotte salvate» mostra le cartelle salvate (massimo 5) e «Le mie bozze».
- **Riga novità.** Una sola, per un aggiornamento disponibile («Vedi e aggiorna») o appena installato («Guarda le novità»).
- **Niente sovrapposizioni.** Le notifiche aspettano: alla chiusura compare solo l'ultima. Gli avvisi di aggiornamento e di Novità compaiono dopo l'ingresso. `reopenOnFirstInteraction` ignora i clic nella pagina.
- **Prima del disegno.** Uno script in testa nasconde `#app` (classe `welcome-pending`, con rete di sicurezza di 4 s), così l'app non lampeggia prima della pagina.
- **Come si entra e come si spegne.**
  - Clic fuori dalle scritte o Esc per entrare.
  - Si spegne con «Non mostrare all'avvio» oppure in Impostazioni › Documenti › Apertura › Pagina di benvenuto (`settings.welcomePage`).
  - Compare una volta per scheda (sessionStorage `itaca-welcome-seen`).
- **Da provare dall'utente:** da file:// con una cartella ricordata deve comparire un solo permesso del browser.

Correzioni dopo la prova dell'utente:
- Le montagne «fluttuavano»: l'orizzonte veniva calcolato una volta sola e la scena saliva quando le scritte sotto crescevano (rotte, novità). Ora un ResizeObserver su pagina, scena e scritte, più `fonts.ready`, lo ricalcola.
- «Riprendi il viaggio» cambiava dimensione: la riga mostra solo la cartella (niente documento), e prima di aprire la pagina si legge la cartella ricordata (`welcomePreset`, al massimo 0,5 s). Il pulsante nasce già giusto e ha una larghezza minima.
- Rotte salvate: titolo centrato tra due trattini, pulsanti più ariosi. La cartella delle bozze ora c'è: veniva letta dopo l'avvio, adesso, se manca, la si chiede direttamente.
- In alto a destra: versione «Itaca Lite X.Y.Z» e pulsante del tema chiaro/scuro (`#welcomeTheme` usa `#themeToggle`; disattivo con Natale).

**Fase 3 fatta (25/11/2026)**, come nella sezione 3:
- Il logo della testata si nasconde (`html.welcome-landing`), poi le animazioni di scena e testata si fermano nella stessa fase (stesso `currentTime`).
- Il disegno vola lungo un arco: 24 fotogrammi WAAPI, solo `transform`, 1,05 s. Cielo, mare e scritte sono livelli propri che sfumano.
- All'atterraggio, nello stesso fotogramma: chiusura del dialog, logo vero visibile, animazioni che ripartono.
- Senza logo visibile (barra chiusa, finestra stretta): dissolvenza.
- Verificato: fasi identiche (es. lg-bob 1483 ms in entrambi) e un solo logo per tutto il volo.

Resta la **Fase 4** (verifica generale). Da provare dall'utente: da file:// con una cartella ricordata, un solo permesso.

Ritocchi dopo la seconda prova:
- **Vela «bucata» in alto.** Il bordo superiore stava 6–8 unità sotto il pennone (fessura chiara). Ora la vela sale sotto il pennone (283,95 → 470,46) e i bordi partono dal suo centro (283,98.6 e 470,49).
- **Vela col vento.** Prima si allargava dal centro (`scale(1.17, 1.05)`) e si staccava. Ora è legata al pennone: `skewX(8deg) scaleY(1.05)` attorno a 380,73, ferma in alto e gonfia in basso. Icona di Finder rigenerata.
- **Versione e tema.** Stanno in basso a destra, come nell'app: il pulsante del tema coincide con `#themeToggle` (`--wl-corner-*` calcolate da `placeWelcomeHorizon`). Sotto 640 px salgono in alto, per non coprire le scritte.

**Fase 4 fatta (25/11/2026).** Problemi trovati e corretti:
- **Barra laterale a destra.** Il pulsante del tema dell'app non è nell'angolo: versione e tema del benvenuto finivano a metà in basso, addosso a «Non mostrare all'avvio». Ora, se `#themeToggle` dista più di 48 px dal bordo destro, la pagina usa l'angolo (stessa distanza dal fondo).
- **Nuvole e stelle.** Seguivano il logo solo all'apertura: con la finestra in secondo piano o «riduci movimento» acceso dopo continuavano. Ora `applyLogoMotion()` mette `.still` anche sul benvenuto (`!logoAwake()`), e `.still` mette in pausa invece di togliere l'animazione (prima le nuvole tornavano tutte sul bordo sinistro).
- **Tastiera.** Il fuoco iniziale andava sul pulsante del tema (primo nel codice): Invio cambiava tema invece di entrare. Ora `autofocus` su «Riprendi / Scegli la cartella» e `.wl-top` sta dopo le scritte (ordine del Tab = ordine visivo).
- **Ricerca nelle Impostazioni.** «intro», «schermata», «introduzione» trovano la Pagina di benvenuto.

Verificato senza problemi: tutte le tavolozze in chiaro e scuro (logo con colori propri, leggibile su ogni barra laterale), Natale (solo scuro: tema del benvenuto disattivato come `#themeToggle`), volo verso la barra a destra, Ripristina (welcomePage, logoMotion, brandSize tornano ai predefiniti), console senza errori.

**Remi (25/11/2026, richiesta dell'utente).** Prima: 5 scalmi e 5 aste, ma solo 4 pale, spostate di un posto (l'asta di sinistra senza pala), più ripide delle aste; le aste partivano sotto i buchi.
- Ogni remo è un pezzo unico `g.lg-oar` dentro `.lg-oars`: asta (`lg-detail`, dal centro dello scalmo) + pala affusolata sullo stesso asse (pendenza −0,55, punta a y 522, come prima). Pala davanti al timone con un margine anche a fine colpo.
- Scalmi `.lg-ports`: buco scuro r 11 con bordo `--lg-sand2`, così il remo sembra entrare nello scafo.
- Niente voga: provata (rotazione attorno allo scalmo) e tolta su richiesta dell'utente. I remi restano fermi e seguono solo l'ondeggiamento della barca.
- Favicon e icone piccole: solo le pale (asta e scalmi sono `lg-detail`). Icona di Finder rigenerata.

