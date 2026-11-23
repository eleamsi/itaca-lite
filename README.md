# Itaca Lite

Itaca Lite è un editor Markdown locale in un unico file HTML. Offre una modalità visuale e una sorgente Markdown, supporta le estensioni di Material for MkDocs e permette di esportare i documenti in PDF o in Word e la cartella in un sito HTML statico.

## Avvio

1. Scarica `Itaca Lite.html` e aprilo in Chrome o Edge.
2. Al primo avvio usa **Scegli cartella** per selezionare la cartella dei documenti `.md` (di solito quella che contiene Itaca) e consenti la modifica dei file: il browser chiede un solo permesso, valido per lettura e scrittura.
   Agli avvii successivi Itaca riapre da sola l’ultima cartella, sul **documento iniziale**: `index.md` se esiste (altrimenti `README.md` o il primo documento), oppure quello che hai scelto in **Impostazioni › File › Documento iniziale** (scrivi il nome e scegli tra i suggerimenti; casella vuota = predefinito) o con **⋯ › Apri all’avvio** su un documento. La scelta vale per quella cartella e segue il documento se lo rinomini o lo sposti. Se il browser ha dimenticato il permesso, basta un clic o un tasto qualsiasi per concederlo di nuovo; scegli **Consenti a ogni visita**, se il browser lo propone, per non doverlo più ripetere.
3. Seleziona un documento dalla barra laterale. Le cartelle hanno l’icona piena colorata e il nome in grassetto; i documenti l’icona del foglio, con l’estensione `.md` attenuata. Linee sottili mostrano a quale cartella appartiene ogni voce.

## File della cartella

La barra laterale mostra **tutti i file** della cartella, non solo i documenti Markdown. Ogni tipo ha un’icona e un colore propri per riconoscerlo a colpo d’occhio: immagini, PDF, documenti di testo (Word, ODT, RTF), fogli di calcolo (Excel, CSV), presentazioni, archivi (ZIP, RAR, 7z), audio, video, codice e configurazioni (JS, Python, HTML, JSON, YAML…) e testo semplice; gli altri hanno un’icona generica.

- Clic su un documento Markdown: si apre in Itaca. Clic su un’immagine: anteprima. Clic su PDF, testo, audio o video: si apre in una nuova scheda; gli altri file vengono scaricati.
- Il menu **⋯** permette di rinominare (l’estensione resta se non ne scrivi un’altra), spostare, duplicare, eliminare, copiare il percorso e vedere le **Informazioni** di qualsiasi file o cartella (vedi **Gestire file e cartelle**).
- Passando sopra un file, il suggerimento mostra percorso, dimensione e data dell’ultima modifica.
- La ricerca nel testo riguarda solo i documenti Markdown.

L’elenco **si aggiorna da solo**: file e cartelle creati, rinominati o eliminati fuori da Itaca compaiono o spariscono in pochi secondi (su Windows entro una ventina di secondi, e più di rado se la cartella è lenta, per esempio di rete), e subito quando torni sulla finestra. Il pulsante **Aggiorna** accanto al nome della cartella resta per forzare una nuova lettura (e per ricaricare le cartelle importate, che sono una copia e non si aggiornano da sole).

## Gestire file e cartelle

Tutto quello che serve per organizzare la cartella si fa dall’elenco, senza pulsanti in più.

- **Trascina una voce** su una cartella per spostarla lì (sul nome di un file: nella sua cartella; nello spazio vuoto in fondo: nella cartella principale). Tenendo premuto **Alt** (**⌥** su Mac) la copi invece di spostarla. La cartella di destinazione si evidenzia con un tratteggio e un’etichetta in basso dice cosa succederà («Sposta in…», «Copia in…»); fermandoti un attimo su una cartella chiusa, si apre. I collegamenti vengono aggiornati come indicato in **Impostazioni › File › Aggiorna i collegamenti**. Si aggiornano sia i collegamenti che puntano all’elemento spostato, sia quelli scritti dentro il documento spostato: un collegamento relativo come `Appunti/Idee.md` diventa `../../Appunti/Idee.md`, così funziona anche in MkDocs e nel sito esportato.
- **Selezione multipla**: `Ctrl + clic` (`⌘ + clic` su Mac) aggiunge o toglie un elemento, `Maiusc + clic` o `Maiusc + ↑/↓` prende un intervallo, `Ctrl/⌘ + A` tutti quelli visibili. Sotto l’elenco compare una barra con il numero degli elementi e i pulsanti **Sposta…** ed **Elimina**; anche `M` e `Canc` (`⌘ + Backspace` su Mac) agiscono su tutti, e trascinandone uno si spostano (o con **Alt** si copiano) tutti insieme. Le cartelle selezionate portano con sé il contenuto. Per eliminare più elementi la seconda conferma chiede di scriverne il numero. `Esc` o un clic semplice annullano la selezione.
- **Trascina file e cartelle dal computer** (Finder, Esplora risorse) sull’elenco: vengono copiati nella cartella sotto il puntatore, con tutte le sottocartelle. Se un nome è già usato il nuovo diventa «Nome (2).pdf». Gli elementi aggiunti lampeggiano per un attimo. Lo stesso fa **⋯ › Aggiungi file qui…**.
- **Trascina un file dall’elenco nel documento** (in Modifica): diventa un collegamento nel punto di rilascio, oppure un’immagine se è un’immagine.
- **Informazioni** (**⋯** o `Ctrl/⌘ + I`): tipo, dimensione, data dell’ultima modifica e posizione; per i documenti anche parole e tempo di lettura, titoli, collegamenti, immagini e quanti documenti li citano; per le immagini le dimensioni in pixel; per le cartelle quanti documenti, file e sottocartelle contengono e lo spazio occupato.
- **Duplica** crea «Nome copia.md» accanto all’originale (anche per le cartelle, con tutto il contenuto).

Con una voce selezionata nell’elenco (clic, oppure `Ctrl/⌘ + Maiusc + E` per andarci dalla tastiera):

| Tasto | Azione |
| --- | --- |
| ↑ ↓ · ← → | Spostati tra le voci · chiudi o apri le cartelle |
| `N` · `Maiusc + N` | Nuovo documento · nuova cartella in quella cartella |
| `F2` | Rinomina |
| `M` | Sposta in un’altra cartella |
| `Ctrl/⌘ + D` | Duplica |
| `Ctrl/⌘ + X`, `C`, `V` | Taglia o copia, poi incolla nella cartella selezionata |
| `Ctrl/⌘ + I` | Informazioni |
| `Ctrl/⌘ + Alt + C` | Copia percorso |
| `Canc` (`⌘ + ⌫` su Mac) | Elimina |

Le stesse scorciatoie sono indicate a destra nel menu **⋯** e nel **Glossario**. Spostare, copiare, rinominare ed eliminare funzionano con le cartelle aperte con **Apri cartella**; in una copia importata si possono solo aggiungere file, che restano nella copia.

## Nuovo documento

- **Nuovo documento** in alto nella barra laterale chiede la **Cartella** (proposta: quella del documento aperto) e il nome. Scrivendo `Sottocartella/Nome` crei anche la sottocartella.
- **Inserimento rapido** (da accendere in **Impostazioni › File**, spento all’inizio): fermati con il puntatore tra due voci dell’elenco. Una linea di puntini si carica dal centro e dopo un secondo l’elenco si apre come un varco nella griglia di puntini del grafo, nei colori del tema, con un **+** al centro; le voci sotto scendono per fare posto. Clicca, scrivi il nome e premi **Invio** (**Esc** annulla). Il documento va nella cartella della voce sopra, oppure dentro di essa se è una cartella aperta. Allontanandoti il varco si richiude.
- Anche il menu **⋯** di una cartella o di un documento ha **Nuovo documento qui**.

## Nuova cartella

- L’icona con la cartella e il **+**, a destra di **Nuovo documento**, chiede dove crearla (**Dentro**) e il nome. Scrivendo `A/B` crei anche le cartelle intermedie.
- Il menu **⋯** di una cartella o di un documento ha **Nuova cartella qui**.
- Nell’**inserimento rapido** tra due voci dell’elenco, un nome che finisce con `/` (per esempio `Archivio/`) crea una cartella invece di un documento.
- La nuova cartella compare aperta; finché è vuota sotto di lei si legge «Cartella vuota». Funziona con le cartelle aperte con **Apri cartella** (non con quelle importate).

**Copia percorso** nel menu **⋯** di un file o di una cartella, oppure l’icona accanto al percorso in basso, copia il percorso completo sul computer (per esempio `/Users/nome/Documenti/docs/Procedure/Guida.md`). Il browser non rivela dove si trova la cartella: se è quella che contiene Itaca lo ricava da solo, altrimenti te lo chiede la prima volta e lo ricorda. Puoi correggerlo in **Impostazioni › File › Percorso della cartella aperta**.

## Cartelle e file

In basso nella barra laterale c’è un solo pulsante, **Cartelle e file**, che apre un menu con:

- le **cartelle salvate** (vedi sotto) e, se la cartella aperta non lo è ancora, **Salva «nome»**;
- **Apri cartella…**: lavori direttamente sui file della cartella (Chrome ed Edge);
- **Apri file…**: un singolo documento Markdown;
- **Importa una copia…**: legge una copia della cartella, utile nei browser che non permettono di aprirla in scrittura (Firefox, Safari);
- **Salva cartella altrove…**, solo con una copia importata (vedi sotto).

## Cartelle importate

Una cartella importata è una **copia in memoria**: Itaca non può scrivere nella cartella originale. Puoi leggere, cercare e modificare i documenti, ma **Salva** scarica il singolo `.md` nella cartella Download; allegati, nuove cartelle, rinomina, spostamento ed eliminazione non sono disponibili e l’elenco non si aggiorna da solo. I file trascinati dal computer nell’elenco si aggiungono alla copia (e partono con **Salva cartella altrove…**).

Per portare via tutto il lavoro usa **Cartelle e file › Salva cartella altrove…**:

- in **Chrome ed Edge** scegli dove salvarla: Itaca crea lì la cartella con tutti i file (anche quelli non Markdown, le cartelle vuote, i documenti nuovi e le modifiche non salvate del documento aperto) e da quel momento lavora su di lei come con **Apri cartella**, quindi Salva scrive sul disco;
- in **Firefox e Safari** la voce diventa **Scarica la cartella (ZIP)**: scarica un archivio con lo stesso contenuto, da estrarre dove vuoi; la copia importata resta aperta.

## Cartelle salvate

Se lavori spesso con le stesse cartelle, salvale per riaprirle senza cercarle ogni volta.

- Con una cartella aperta, premi la **stella** accanto al suo nome in cima all’elenco. La stella piena indica che è già salvata; premila di nuovo per toglierla.
- Il menu **Cartelle e file**, in basso nella barra laterale, elenca le cartelle salvate: clic sul nome per aprirla. Passando sopra una voce compaiono **Modifica** (cambia il nome nell’elenco o, con **Cambia cartella…**, la cartella sul disco) e **×**, che la toglie dall’elenco senza toccare i file.
- Il browser può chiedere di nuovo il permesso quando apri una cartella salvata.
- Due cartelle con lo stesso nome in posti diversi si possono salvare entrambe: la seconda compare come «Nome (2)». I nomi nell’elenco devono essere tutti diversi.
- Se una cartella salvata **non risponde** (il browser conserva un riferimento alla cartella che, per esempio dopo un cambio di rete, può rovinarsi), Itaca propone di **sceglierla di nuovo** — la voce salvata viene aggiornata — o di toglierla dall’elenco. Se l’elenco non si riesce a salvare, Itaca trova le voci rovinate e propone di toglierle, conservando le altre.

### Cartelle di rete

Itaca funziona anche con le cartelle condivise (`\\server\condivisione`). Se la rete è lenta o cambia (per esempio passando dall’ethernet alla WiFi):

- **Cartelle e file** si apre sempre, e puoi scegliere un’altra cartella anche mentre una è in apertura;
- un file che non risponde entro 30 secondi mostra un avviso invece di bloccare Itaca;
- durante un cambio di rete Itaca sospende per qualche secondo le letture automatiche.

## Ricerca nei documenti

La casella **Cerca nei documenti…** in alto nella barra laterale (`Ctrl/⌘ + K`) cerca nei nomi, nelle cartelle e nel testo di tutti i documenti della cartella.

- Non distingue maiuscole e accenti: `perche` trova anche «Perché». Più parole valgono prima di tutto come **frase**, senza virgolette: `motore principale` mostra per primi i documenti che contengono proprio «motore principale» (evidenziato per intero), poi quelli che hanno le due parole sparse; sopra i risultati Itaca dice quanti hanno la frase intera. Con le virgolette decidi tu: `"motore principale" pompa` cerca la frase e la parola, ovunque siano.
- Ogni risultato mostra la sezione in cui si trova (§ titolo), quante volte compare e un estratto. Clic sul risultato per aprirlo sulla prima occorrenza; clic di nuovo per passare alla successiva.
- Tastiera: **Invio** apre il primo risultato, **↓/↑** scorrono i risultati, **Esc** torna alla casella o la svuota.
- I file cambiati fuori da Itaca (da un altro programma o da un altro utente) vengono riletti alla ricerca successiva.

## Scrivere in Markdown

In **Modifica** puoi usare la barra di formattazione oppure scrivere direttamente in Markdown e Material per MkDocs: la sintassi diventa formattazione appena è completa e vedi subito il risultato. Se una conversione non ti serve, `Ctrl/⌘ + Z` la riporta al testo scritto.

- **Inizio riga** (dopo lo spazio): `#` … `######` titoli, `-` `*` `+` elenco puntato, `1.` elenco numerato (anche da un altro numero), `>` citazione, `[ ]` / `[x]` casella da spuntare.
- **Nel testo** (alla chiusura, o al più tardi con lo spazio o la punteggiatura che seguono): `**grassetto**`, `*corsivo*`, `_corsivo_`, `` `codice` ``, `~~barrato~~`, `==evidenziato==`, `^^inserito^^`, `++ctrl+s++` tasti, `H~2~O` pedice, `x^2^` apice, `[testo](indirizzo)`, `![immagine](percorso)`, `[[documento]]`.
- **Blocchi** (con **Invio**): ` ``` ` o ` ```python ` blocco di codice, `---` linea di separazione, `!!! note "Titolo"` / `??? tip` ammonimenti, `=== "Scheda"` schede, `> [!NOTE]` riquadro, `| Nome | Valore |` tabella con intestazione.
- **Invio su una riga vuota** in fondo a citazione, riquadro, ammonimento o sezione espandibile esce dal blocco.
- **Backspace a inizio riga** toglie il segno: una casella torna voce d'elenco, una voce torna paragrafo (o sale di un livello), un titolo torna paragrafo, la prima riga di una citazione ne esce. Unendo due righe (Backspace a inizio riga o `Canc` a fine riga) il testo prende il formato della riga sopra. `Ctrl/⌘ + Z` annulla anche questi passaggi.
- **Tab** e **Maiusc + Tab** in un elenco spostano la voce di un livello più dentro o più fuori.
- **Uscendo dalla riga** (Invio, frecce, clic altrove) quello che è rimasto scritto in Markdown nella riga in cui hai scritto viene convertito (spostarsi soltanto su una riga non la cambia). Se annulli una conversione con `Ctrl/⌘ + Z`, quella riga resta com'è.
- **Suggerimenti**: scrivendo `[[` compare l'elenco dei documenti (con `#` le loro sezioni); dentro le parentesi di `[testo](` e `![immagine](` l'elenco dei file e delle immagini della cartella. Frecce per scegliere, **Invio** o **Tab** per inserire, **Esc** per chiudere. Il percorso viene scritto relativo al documento aperto, anche con spazi nel nome.
- **Documenti che non esistono**: un collegamento a un documento mancante è tratteggiato; un clic (in Lettura, o `Ctrl/⌘ + clic` in Modifica) crea il documento nella stessa cartella e lo apre.
- **Chiudi automaticamente** (Impostazioni › Documenti, spento all'inizio): scrivendo `*`, `_`, `` ` ``, `[` o `(` viene aggiunta subito la chiusura e il cursore resta in mezzo; scrivendo la chiusura la si scavalca, e `Backspace` su una coppia vuota la cancella tutta. Uno spazio subito dopo `*` o `` ` `` toglie la chiusura aggiunta (così `* ` a inizio riga resta un elenco), e ` ```js ` o `***` funzionano come senza chiusura automatica. Con del testo selezionato, il segno lo racchiude (anche `=` e `~`; un secondo `*` fa il grassetto) e la formattazione compare appena sposti il cursore.
- **Incolla**: un testo in Markdown (per esempio da un editor di codice) viene mostrato già formattato; **Incolla senza formattazione** lo lascia com'è.

**Lettura** serve solo a leggere; **Markdown** mostra e modifica il sorgente, senza anteprima. Si disattiva in **Impostazioni › Documenti › Markdown mentre scrivi**.

## Notifiche

I messaggi (documento salvato, errori, avvisi) compaiono in alto al centro del documento, in una piccola etichetta con un'icona colorata: verde per le operazioni riuscite, ambra per gli avvisi, rossa per gli errori. Se la barra di Lettura/Modifica occupa il centro, l'etichetta si sposta alla sua sinistra (o appena sotto, nelle finestre strette); sopra una finestra aperta compare al centro dello schermo. Scompare da sola dopo qualche secondo.

## Barra di formattazione

Compare in basso quando sei in **Modifica**. I comandi delle tabelle (righe, colonne, allineamento) compaiono solo con il cursore in una tabella; **Blocchi** contiene riquadro, sezione espandibile e i blocchi Material for MkDocs. Il pulsante **Linea di separazione** inserisce una riga orizzontale (`---`) dopo il paragrafo in cui si trova il cursore. I titoli non hanno più una linea automatica sopra: le separazioni le metti tu dove servono. Il pulsante **Casella da spuntare** aggiunge o toglie la casella sulla riga: fuori da una tabella crea una voce di elenco con la casella (`- [ ]`), in una cella di tabella mette la casella nella cella. Sugli schermi stretti la barra è una sola riga che scorre in orizzontale, con il bordo sfumato dove ci sono altri comandi.

## Collegamenti

In **Lettura**, passando sopra un collegamento a un documento ne vedi l’anteprima; un clic lo apre.

In **Modifica** un clic su un collegamento apre subito il riquadro per modificarlo (per aprirlo: `Ctrl/⌘ + clic` oppure il pulsante **Apri** del riquadro). Il pulsante 🔗 della barra di formattazione apre lo stesso riquadro per un nuovo collegamento, o per quello in cui si trova il cursore.

- Una sola casella: mentre scrivi compaiono i **suggerimenti** tra **tutti i file** della cartella (documenti, PDF, immagini, video, fogli di calcolo…), con l’icona del tipo e la cartella. `↑ ↓` per scegliere; **Invio** (o un clic) **scrive** il suggerimento nella casella e, per un documento, ne elenca subito le **sezioni**; un altro **Invio** (o **Inserisci**) crea il collegamento. Così puoi scegliere il documento e poi aggiungere `#` e la sezione senza riaprire il riquadro.
- Puoi anche incollare un **indirizzo web** (`https://…`, `www.…`, un indirizzo e-mail), scrivere un percorso o `[[Documento]]`.
- Per collegare una **sezione**: `#` seguito dal titolo per il documento aperto (`#installazione`), oppure nome del documento, `#` e titolo (`procedure#uso`).
- Inserendo o modificando un collegamento la pagina resta dove sei.
- **Testo** è il testo del collegamento: se lo lasci vuoto si usa il nome del file.
- **Rimuovi** toglie il collegamento lasciando il testo (`Ctrl/⌘ + Z` lo ripristina).
- **Esc**, **Annulla** o un **clic fuori dal riquadro** chiudono senza cambiare nulla.

**Collegamento o immagine?** Il pulsante 🔗 crea un **collegamento** (anche a un'immagine: nel testo resta una parola cliccabile). Il pulsante **Immagine** apre lo stesso riquadro ma per **mostrare** l'immagine nel documento: la ricerca elenca solo le immagini della cartella (senza ricerca, prima quelle vicine al documento), accetta l'indirizzo di un'immagine sul web e in fondo ha **Scegli un'immagine dal computer…** (copiata in `_allegati` al salvataggio). La casella **Descrizione** è il testo alternativo; se la lasci vuota vale il nome del file.

### Percorsi di rete

I percorsi delle cartelle condivise si scrivono così come sono, `\\server\condivisa\progetto`, oppure tra `< >` se contengono spazi (`<\\server\Progetti 2024\Impianto>`); vanno bene anche gli indirizzi `file://…`. Itaca li mostra con l’icona della rete e in **Lettura** un clic **copia il percorso** (in **Modifica** `Ctrl/⌘ + clic`; un doppio clic lo modifica): il browser non apre le cartelle di rete da una pagina, ma incollato in Esplora file o nel Finder il percorso ci porta subito.

- **Incollando** un percorso di rete (anche tra virgolette, come lo copia Esplora file) diventa subito un percorso cliccabile; scrivendolo a mano si converte alla chiusura di `>` o lasciando la riga.
- Nel riquadro dei **collegamenti** puoi scrivere `\\server\cartella` o `C:\cartella`: il collegamento diventa `file://…` e anche lui, cliccato, copia il percorso.
- Nel sito esportato restano collegamenti `file://`.

## Video

Incollando nel documento l’indirizzo di un video (**YouTube**, **Vimeo**, **Dailymotion**, **Loom**, **Twitch**, **TikTok** o un file `.mp4`, `.webm`, `.mov`…) Itaca inserisce un collegamento con un testo leggibile, ad esempio «▶ Video su YouTube», invece dell’indirizzo per intero; se prima selezioni del testo, il collegamento va su quel testo. Il video si apre con un clic in **Lettura** (o `Ctrl/⌘ + clic` in **Modifica**). Il testo si cambia come per ogni collegamento.

Itaca è aperta come file (`file://`): da lì i lettori di YouTube e degli altri servizi rifiutano di essere mostrati dentro la pagina, perciò i video di questi siti restano collegamenti. I **file** video e audio invece (scaricati nella cartella o indirizzi web che finiscono in `.mp4`, `.mp3`…) si guardano e si ascoltano dentro il documento: vedi [Video e audio incorporati](#video-e-audio-incorporati).

## Allegati

Oltre alle immagini puoi inserire file di qualsiasi tipo (PDF, Word, Excel, archivi…): **incollali** dopo averli copiati dal Finder o da Esplora risorse, **trascinali** nel punto del testo che vuoi, oppure usa il pulsante 📎 della barra di formattazione. Nel testo compare un collegamento con il nome del file; al salvataggio il file viene copiato in `_allegati` (se il nome è già usato diventa «Nome (2).pdf»).

Sotto il collegamento compare la scelta **Collegamento** (resta com’è) o **Anteprima** — **Lettore** per video e audio: il file diventa una [scheda](#schede-dei-file) o un [lettore](#video-e-audio-incorporati) dentro il documento. Un tasto o un clic altrove chiudono la scelta lasciando il collegamento; la stessa trasformazione si fa dopo con il pulsante **Anteprima** (o **Lettore**) del riquadro del collegamento. PDF, Word e file di testo diventano subito un riquadro incorporato, come spiegato sotto.

Aprendo il collegamento (clic in **Lettura**, **Apri** nel riquadro del collegamento in **Modifica**) PDF, testi, audio e video si aprono in una nuova scheda; gli altri file vengono scaricati.

### PDF incorporati

I **PDF** si possono leggere direttamente dentro il documento: un PDF incollato, trascinato (dal computer o dall’elenco dei file) o scelto con 📎 compare come un riquadro con il visualizzatore del browser (pagine, zoom, rotazione, scarica, stampa) e, in alto, il titolo e il pulsante **Apri**, che apre il PDF in una nuova scheda.

Trascinando un PDF nel documento una **linea** indica tra quali righe verrà inserito (per gli altri file un cursore lampeggiante indica il punto nel testo).

Il PDF si comporta come un blocco unico: **Backspace** dalla riga sotto (o **Canc** da quella sopra) e le frecce lo **selezionano** (contorno colorato), e una riga vuota accanto viene tolta; solo un secondo Backspace/Canc lo elimina (`Ctrl/⌘ + Z` lo rimette). Con il PDF selezionato **Invio** o la scrittura proseguono nella riga sotto; anche un clic sul titolo lo seleziona. Se ci sono più riquadri uno dopo l'altro (PDF, schede delle pagine web, lettori), le frecce passano dall'uno all'altro senza aggiungere righe vuote in mezzo; una riga creata solo per il cursore sparisce se la lasci vuota.

In **Modifica** c’è anche **Collegamento**, che riporta il PDF a un semplice collegamento; al contrario, il riquadro di un collegamento a un PDF ha il pulsante **Incorpora**. Il riquadro si può allungare o accorciare trascinando l’angolo in basso a destra.

Nel Markdown un PDF incorporato è un’immagine che punta a un PDF, **da sola su una riga** (si può scrivere anche a mano, si trasforma appena chiudi la parentesi):

```markdown
![Manuale d’uso](_allegati/manuale.pdf)
![Manuale d’uso](_allegati/manuale.pdf#page=3)
![[manuale.pdf]]
```

`#page=3` apre il PDF alla pagina indicata. Nel PDF esportato compare solo il titolo; nel sito HTML esportato il PDF resta incorporato, con il link Apri.

### Documenti Word incorporati

Allo stesso modo si possono incorporare i **documenti Word** (`.docx`): incollati, trascinati o scelti con 📎 compaiono in un riquadro con un’**anteprima delle pagine** (testo, stili, tabelle, immagini, intestazioni e piè di pagina), rimpicciolite se serve per stare nella larghezza del documento. In alto ci sono **Apri** (l’anteprima in una nuova scheda), **Scarica** (il file `.docx`, per aprirlo con Word) e, in Modifica, **Collegamento**. Anche un semplice collegamento a un `.docx`, o un clic sul file nell’elenco, apre l’anteprima in una nuova scheda, con in alto il pulsante **Scarica**. Cursore, selezione, trascinamento e **Incorpora** funzionano come per i PDF.

```markdown
![Relazione annuale](_allegati/relazione.docx)
![[relazione.docx]]
```

L’anteprima è in sola lettura e preparata da Itaca, senza Word né Internet: caratteri non installati, caselle di testo, forme, revisioni e commenti possono apparire semplificati e le pagine non sempre si interrompono come in Word. I vecchi file **.doc** (Word 97–2003) non si possono mostrare: restano un collegamento. Nel PDF esportato compare solo il titolo; nel sito HTML esportato il riquadro ha il link **Scarica**.

### File di testo incorporati

Anche i **file di testo** si possono incorporare: `.txt`, `.log`, `.csv`, `.tsv`, `.json`, `.xml`, `.yaml`, `.toml`, `.ini`, `.sql` e i file di codice (`.py`, `.js`, `.sh`, `.html`, `.css`…). Incollati, trascinati o scelti con 📎 diventano un riquadro con il contenuto: numeri di riga e colori della sintassi per codice e log, testo a capo per i `.txt`, una **tabella** per CSV e TSV, JSON su una sola riga mostrato indentato. Il riquadro è alto quanto il contenuto (fino a un massimo) e segue il tema chiaro o scuro.

Come per Word ci sono **Apri** (anteprima in una nuova scheda, con **Scarica** in alto), **Scarica** e, in Modifica, **Collegamento**. Anche un clic sul file nell’elenco o su un collegamento apre l’anteprima. Dei file molto grandi il riquadro mostra solo l’inizio.

Per **SVG** e **HTML** in alto c’è anche la scelta **Anteprima / Codice**: l’anteprima mostra l’immagine o la pagina come appare, il codice il sorgente con i colori della sintassi (la scelta vale anche per Apri). La pagina HTML viene mostrata isolata: i suoi script funzionano, ma non possono leggere Itaca né i tuoi documenti; fogli di stile e immagini che la pagina prende da altri file della cartella non vengono caricati.

```markdown
![Configurazione](_allegati/config.yaml)
![[registro.log]]
```

**Modificare il file.** In Modifica il pulsante **Modifica** del riquadro apre il contenuto del file in una finestra con i numeri di riga (`Tab` rientra come il resto del file, `Ctrl/⌘ + Invio` o `Ctrl/⌘ + S` applica). Le modifiche si vedono subito nel riquadro ma il file viene **scritto quando salvi il documento**, come il resto delle modifiche: fino ad allora il documento risulta modificato e **Non salvare** le scarta. `Ctrl/⌘ + Z` nel documento riporta il riquadro alla versione di prima (`Ctrl/⌘ + Maiusc + Z` la rifà); se annulli dopo aver salvato e salvi di nuovo, il file torna com’era. Itaca conserva **codifica** (UTF-8, con o senza BOM, oppure Windows-1252 «ANSI», comune negli script di Windows e di iFix) e **fine riga** (CRLF di Windows o LF) del file; se scrivi caratteri che la codifica ANSI non ha, chiede se salvare il file in UTF-8. Se nel frattempo un altro programma ha cambiato il file, prima di sovrascriverlo chiede conferma. Serve la cartella di lavoro aperta con il permesso di scrittura.

**Nel documento.** Il pulsante **Nel documento** porta il contenuto dentro il documento, senza più collegamento al file: diventa un **blocco di codice** con il linguaggio giusto e il nome del file come titolo; un CSV o TSV può diventare una **tabella** (ordinabile e filtrabile in Lettura) o restare testo. Per la tabella si sceglie se **la prima riga contiene i titoli delle colonne**: Itaca lo propone da sé guardando la prima riga (celle tutte piene, nomi diversi, nessun numero); se non la spunti anche la prima riga è un dato e le colonne si chiamano «Colonna 1», «Colonna 2» e così via. Il file resta nella cartella; `Ctrl/⌘ + Z` riporta il riquadro. Se il file aveva modifiche non ancora salvate, nel documento finisce la versione modificata e il file non viene toccato.

In Modifica, nei riquadri stretti, i pulsanti mostrano solo l’icona (il nome compare passandoci sopra).

### Video e audio incorporati

I **video** (`.mp4`, `.mov`, `.m4v`, `.webm`, `.mkv`, `.ogv`) si guardano dentro il documento con il lettore del browser: riproduzione, volume, velocità, schermo intero. I file **audio** (`.mp3`, `.wav`, `.m4a`, `.aac`, `.ogg`, `.opus`, `.flac`) hanno un lettore di Itaca con la **forma d’onda** del file: clic o trascinamento sulla forma d’onda per spostarsi, frecce `←/→` per 5 secondi avanti o indietro, `Spazio` per avviare o fermare, il pulsante **1×** cambia la velocità (1,25×, 1,5×, 2×, 0,75×). Suona un lettore alla volta: avviandone uno, gli altri si fermano.

**Il lettore di Itaca.** Un audio avviato continua a suonare anche se apri un altro documento: compare il lettore di Itaca, piccolo, con titolo, documento di provenienza (un clic ci riporta), forma d’onda, tempi e **×** per fermare e chiuderlo. In **Impostazioni › Aspetto › Lettore audio** si sceglie come appare:

- **Nella barra** (predefinito): nella barra laterale, sopra **Cartelle e file**. Se la barra laterale è nascosta passa nell’angolo.
- **Fluttuante**: sopra al documento, si trascina dove vuoi dalla maniglia a puntini; Itaca ricorda la posizione.
- **Nell’angolo**: in basso a destra; con la freccia si riduce a un piccolo disco (l’anello mostra l’avanzamento, le barrette si muovono mentre suona) e un clic lo riapre.
- **Spento**: nessun lettore, l’audio si ferma quando cambi documento.

I tasti multimediali della tastiera (play/pausa) comandano il lettore.

Anche gli **indirizzi web** di file audio e video (`https://…/intervista.mp3`) funzionano: incollati su una riga vuota propongono **Collegamento** o **Lettore**. Le pagine di YouTube e simili restano collegamenti (vedi [Video](#video)).

```markdown
![Presentazione del progetto](_allegati/presentazione.mp4)
![Intervista](_allegati/intervista.mp3)
![Podcast](https://esempio.it/puntata-12.mp3)
![Dal minuto 1:30](_allegati/lezione.mp4#t=90)
```

Il browser legge i formati più diffusi; un `.mkv` si vede se il video è H.264, VP9 o AV1 (i casi più comuni). Formati come `.avi`, `.wmv`, `.wma`, `.aiff` o codifiche rare il browser non li sa riprodurre: il riquadro lo dice e **Scarica** porta il file su un programma che li legge. **Apri** mostra il video in una nuova scheda (l’audio non ne ha bisogno: c’è il lettore); cursore, selezione, trascinamento e **Collegamento** funzionano come per i PDF. Nel PDF esportato compare solo il titolo, nel sito HTML esportato il lettore resta.

### Schede dei file

Un file che Itaca non mostra dentro il documento (**archivi ZIP**, Excel, presentazioni, programmi…) può comparire come **scheda**: icona del tipo con l’estensione, titolo, tipo e dimensione del file. Per gli **ZIP** la scheda dice anche quanti file contiene e il pulsante **Contenuto** (in Lettura basta un clic sulla scheda) mostra l’elenco dei file dell’archivio con cartelle e dimensioni, senza estrarlo. **Scarica** scarica il file, **Apri** lo apre nel browser se sa mostrarlo, in Modifica **Collegamento** torna al semplice link.

```markdown
[Materiale del corso](_allegati/materiale.zip){ .card }
[Budget 2026](../Finanza/budget.xlsx){ .card }
```

È la stessa sintassi delle schede delle pagine web, con il percorso di un file al posto dell’indirizzo. In MkDocs la riga resta un normale collegamento.

### Schede delle pagine web

Incollando l’indirizzo di una pagina web **su una riga vuota**, sotto compare la scelta **Collegamento** (come prima) o **Scheda**. La scheda è un riquadro compatto con l’icona del sito, il titolo e l’indirizzo: in Lettura un clic la apre in una nuova scheda del browser, in Modifica ci sono **Apri** e **Collegamento** per tornare al semplice link. Anche il riquadro di un collegamento a una pagina web ha il pulsante **Scheda**.

```markdown
[Documentazione di Python](https://docs.python.org/3/){ .card }
```

Il titolo proposto viene dall’indirizzo (Itaca non legge la pagina): si cambia con un doppio clic sulla scheda in Modifica o nel Markdown. L’icona è quella del sito, chiesta al sito stesso; se non c’è compare l’iniziale. In MkDocs la riga resta un normale collegamento.

## Tabelle

**Da Excel**: copia le celle in Excel (o LibreOffice, Numbers, Fogli Google) e incollale in **Modifica**: diventano una tabella Markdown pulita, con la prima riga come intestazione (se è fatta solo di numeri Itaca aggiunge «Colonna 1, 2…») e le colonne di numeri allineate a destra. Le celle su più righe e le virgolette sono conservate. Incollando **dentro una tabella** le celle riempiono la tabella a partire da quella del cursore, aggiungendo righe e colonne se servono (`Ctrl/⌘ + Z` annulla). Con **Incolla senza formattazione** arriva il testo semplice.

**Tabelle grandi**: oltre 15 righe o con almeno 7 colonne la tabella sta in un riquadro alto al massimo circa mezza pagina, che **scorre** in verticale e in orizzontale; l’intestazione resta ferma in alto e, nelle tabelle larghe, anche la prima colonna resta ferma a sinistra. Le colonne prendono la larghezza del contenuto (fino a un massimo, poi il testo va a capo) invece di schiacciarsi, e le righe sono a colori alterni. Nel PDF la tabella è stampata per intero. Anche con migliaia di righe la scrittura nelle celle resta immediata.

**Eliminare una tabella**: con il cursore in una cella il pulsante **Elimina tabella** della barra di formattazione (accanto a Elimina riga ed Elimina colonna) la toglie tutta; oppure `Backspace` dalla riga sotto (o `Canc` da quella sopra) la seleziona con un contorno e un secondo tasto la elimina, come i PDF e i blocchi di codice. `Ctrl/⌘ + Z` la riporta.

**Con la tastiera, in Modifica**, la tabella si usa come un foglio di calcolo: `Tab` / `Maiusc + Tab` passano alla cella successiva / precedente (selezionandone il contenuto, così si scrive sopra) e `Tab` nell’ultima cella aggiunge una riga; `Invio` scende alla cella sotto, nell’ultima riga aggiunge una riga nuova e un secondo `Invio` sulla riga vuota la toglie ed **esce dalla tabella**; `Maiusc + Invio` va a capo dentro la cella; `↑ ↓` passano alla riga sopra o sotto e oltre il bordo escono dalla tabella.

**In Lettura** un clic sull’intestazione di una colonna la **ordina** (crescente, poi decrescente, la terza volta torna l’ordine originale): numeri anche all’italiana con unità (`1.234,5`, `3,2 bar`, `75 %`), date (`21/11/2026`), testo in ordine alfabetico; le celle vuote restano in fondo. Le tabelle con almeno 6 righe (sulle più corte non serve) hanno sopra una casella per **filtrare** le righe (tutte le colonne o una sola, senza badare ad accenti e maiuscole) e **Azzera**. È comodo per elenchi di tag, allarmi e parametri. Il documento non cambia: tornando in Modifica la tabella è com’era. Si disattiva in Impostazioni › Documenti › **Ordina e filtra le tabelle**.

## Blocchi di codice

Accanto ai tre accenti gravi va il linguaggio, per i colori. Per l’automazione:

- `vba` — VBA di Excel e Access e gli **script di iFix**: oltre a parole chiave e funzioni di VBA riconosce le subroutine di iFix (`OpenPicture`, `ReadValue`, `WriteValue`, `ToggleDigitalPoint`, `AcknowledgeAllAlarms`…), i tag del database (`Fix32.NODO.TAG.F_CV`, anche dentro le stringhe), i nomi delle Sub e le etichette di `On Error GoTo`. Valgono anche `vbs`, `vb6`, `ifix`, `bas`.
- `sql` (standard), `tsql` (SQL Server: `TOP`, `NOLOCK`, `@variabili`, `[nomi]`, `GO`…), `postgresql`, `mysql`, `plsql` (Oracle).

In **Modifica** il pulsante **Opzioni** del blocco imposta il **titolo** o il **nome del file** mostrato sopra il codice, le **righe evidenziate** (`12-15 20`) e il numero da cui parte la numerazione; un clic su un numero di riga evidenzia la riga, `Maiusc + clic` un intervallo dall’ultimo clic (come per selezionare il testo: un altro `Maiusc + clic` lo allunga o lo accorcia). Nel Markdown sono le opzioni di Material for MkDocs:

````markdown
```vba title="Pagina1.bas" hl_lines="12-15"
Private Sub CFixPicture_Initialize()
    OpenPicture "Panoramica.grf"
End Sub
```
````

Come i PDF, il blocco di codice si cancella in due tempi: `Backspace` dalla riga sotto (o `Canc` da quella sopra) lo **seleziona** con un contorno, e solo un secondo `Backspace`/`Canc` lo elimina (`Ctrl/⌘ + Z` lo rimette); anche un clic sulla sua intestazione lo seleziona. Le frecce invece entrano nel codice.

**Copia** copia il codice senza i numeri di riga; `Maiusc + clic` su **Copia** copia solo le righe evidenziate.

## Grafo dei collegamenti

Il riquadro **Grafo dei collegamenti** mostra come i documenti della cartella si collegano tra loro: ogni nodo è un documento, ogni linea un collegamento (in un verso o nell’altro). Il documento aperto ha il colore d’accento del tema, gli altri il colore della loro cartella principale.

- **Locale** mostra il documento aperto e quelli collegati, **Tutto** l’intera cartella (anche i documenti senza collegamenti). La scelta è una sola: vale sia nel riquadro sia nella vista a schermo intero, e cambiandola in una delle due cambia anche nell’altra.
- Trascina un nodo: i documenti collegati lo seguono. Trascina lo sfondo per spostare la vista, usa la rotella per lo zoom, doppio clic sullo sfondo (o `0`) per adattare.
- Passando sopra un nodo si evidenziano i suoi collegamenti; un clic apre il documento.
- **⤢** apre il grafo grande in una finestra, con la legenda delle cartelle.

Come gli altri pannelli, si accende e si sposta da **Impostazioni › Pannelli** oppure trascinandolo (vedi **Spostare i pannelli**).

## Spostare i pannelli

**Indice del documento** e **Citato da** stanno sempre insieme: nella barra laterale oppure in un angolo del documento. Il **Grafo dei collegamenti** ha la sua posizione, ma se anche indice e citazioni sono nel documento sta nel loro stesso angolo e si sposta con loro.

- Per spostarli, tieni premuto il **titolo** di un pannello e trascinalo: compaiono le **zone tratteggiate** dove puoi lasciarlo (la barra laterale e i quattro angoli). La zona sotto il puntatore si evidenzia e una linea mostra dove finirà rispetto agli altri pannelli. **Esc** annulla.
- Spostando l’indice o le citazioni si spostano entrambi; nel documento si sposta tutto il gruppo, grafo compreso. Il grafo portato nella barra laterale si stacca dal gruppo; riportato in un angolo, se indice e citazioni sono nel documento, li raggiunge.
- Trascinando un pannello sopra o sotto gli altri dello stesso posto ne cambi l’**ordine**, che si sceglie anche in **Impostazioni › Pannelli › Ordine**.
- Un semplice clic sul titolo continua ad aprire e chiudere il pannello.
- Nelle finestre strette gli angoli non sono disponibili e i pannelli tornano nella barra laterale.

Al primo avvio l’indice è nella barra laterale, «Citato da» è spento e il grafo è nel documento in alto a destra.

## Modifiche non salvate

Se cambi documento, ricarichi o apri un’altra cartella con modifiche non salvate, Itaca chiede **Salvare le modifiche?**: **Salva** (o `Invio`) salva e prosegue, **Non salvare** scarta le modifiche, **Annulla** (o `Esc`) resta sul documento.

## Più documenti aperti

In **Impostazioni › Documenti › Più documenti aperti** scegli come lavorare con più documenti insieme:

- **Uno** (all'inizio): un documento alla volta, come sempre.
- **Schede**: in alto a sinistra, accanto ai comandi del documento, compare una scheda per ogni documento aperto (nelle finestre strette le schede scendono su una riga propria). Un clic su una scheda la mostra; la **×**, un clic con la rotella o `Alt + W` (`⌥W` sul Mac) la chiude; le frecce **← →** passano da una scheda all'altra.
- **Affiancati**: i documenti stanno uno accanto all'altro, come le pagine di un libro aperto, e si sfogliano scorrendo in orizzontale (trackpad, `Maiusc` + rotella o la barra di scorrimento), con il puntatore in qualunque punto, anche sopra un documento. Una tabella o un blocco di codice più larghi della colonna scorrono prima da soli. `Alt + W` (`⌥W` sul Mac) chiude la colonna attiva, come la **×** sul dorso. Scorrendo, le colonne si fermano una sull'altra lasciando visibile il **dorso** con il titolo in verticale. Un clic su un documento lo rende **attivo**: è quello che puoi modificare e salvare, con il dorso colorato; gli altri restano in lettura. Un clic su un collegamento in un documento non attivo lo attiva e apre il collegamento.

Come si aprono i documenti con le schede o affiancati:

- Un documento scelto nell'**elenco dei file**, nella **ricerca** o nel **grafo** si apre in una scheda nuova (o in una colonna nuova, a destra del documento attivo); se è già aperto viene solo mostrato.
- Un **collegamento** con **Affiancati** apre il documento nella colonna a destra; con **Schede** lo apre nella stessa scheda (`Ctrl/⌘ + clic` in Lettura o clic con la rotella: in una scheda nuova).
- Un **nuovo documento** si apre in una scheda nuova.
- Passando da un documento all'altro le **modifiche non salvate restano**: la scheda o il dorso hanno un pallino; si salvano tornando su quel documento. Chiudendo una scheda con modifiche, o cambiando cartella, Itaca chiede se salvarle. Con il **salvataggio automatico** il documento viene salvato quando lo lasci.
- Ogni documento ricorda il punto in cui eri e il modo (Lettura, Modifica, Markdown).
- Le schede aperte restano per la cartella: alla riapertura di Itaca tornano com'erano.
- Anche l’ultima scheda o colonna si può chiudere: non resta aperto nessun documento. `Alt + Maiusc + W` (`⌥⇧W` sul Mac) o **⋯ › Chiudi tutti** chiude tutto in una volta, chiedendo prima di salvare le modifiche.

**Indice, Citato da e grafo** seguono sempre il documento attivo. Con **Schede** restano dove li hai messi; con **Affiancati** vanno nella barra laterale (gli angoli del documento servono alle colonne) e tornano al loro posto scegliendo un'altra modalità.

## Barra del documento

In alto a destra, da sinistra a destra:

- **Lettura · Modifica · Markdown**: come vedi il documento. In **Lettura** non si può modificare; **Modifica** apre l’editor visuale con la barra di formattazione; **Markdown** modifica il sorgente e compare solo quando sei in **Modifica**. Nelle finestre strette restano solo le icone. `Ctrl/⌘ + E` passa da **Lettura** a **Modifica** e viceversa (dal **Markdown** torna a **Modifica**).
- **Cerca** (`Ctrl/⌘ + F`, o `Ctrl/⌘ + H` con la sostituzione): trova e sostituisci nel documento. La stessa scorciatoia la chiude (se intanto hai selezionato un altro testo nel documento, cerca quello).
- **⋯ Altre azioni**: **Esporta PDF…**, **Esporta in Word…** (vedi [Esportare in Word](#esportare-in-word)), se la cartella è un repository git **Versioni e confronto…** e **Chi ha modificato questo punto…** (vedi [Versioni e confronto con git](#versioni-e-confronto-con-git)), **Chiudi documento** (`Alt + W`, `⌥W` sul Mac) e, con più documenti aperti, **Chiudi tutti** (`Alt + Maiusc + W`, `⌥⇧W` sul Mac). Chiuso l’ultimo documento resta la schermata della cartella: scegline un altro dalla barra laterale.
- **Salva** (`Ctrl/⌘ + S`): compare quando modifichi o quando ci sono modifiche non salvate.

Nella barra in basso il percorso del documento è modificabile: un clic sul **nome del documento** o su una delle sue **cartelle** lo trasforma in una casella (con un percorso lungo ogni cartella si accorcia ma resta cliccabile; il nome completo è nel suggerimento); **Invio** rinomina e aggiorna i collegamenti (come indicato in **Impostazioni › File › Aggiorna i collegamenti**), **Esc** o un clic altrove annullano. L’estensione `.md` resta da sola.

## Caricamento

Se un’operazione richiede un momento, sul documento compare **Apertura di «Nome»…** con una barra che scorre in alto. Succede quando apri un documento molto grande, passi tra Lettura e Modifica in un documento grande, o apri una cartella con molti file. Le aperture veloci non mostrano nulla.

## Immagini allineate

Seleziona un’immagine in **Modifica** e usa il comando di allineamento della barra:

- **A sinistra** / **A destra**: l’immagine si affianca al testo, che le scorre intorno.
- **Al centro**: l’immagine sta da sola al centro della colonna.
- **Senza testo a lato**: l’immagine torna a sinistra, senza testo intorno.

Anche le immagini ridimensionate (salvate come `<img … width="…">`) si possono centrare e allineare. Ciò che è centrato, le linee orizzontali e i titoli principali non restano accanto a un’immagine affiancata: vanno sotto di lei.

## Loki, barchetta o slitta

In fondo al documento può comparire una piccola animazione in pixel art, a scelta in **Impostazioni › Aspetto › Animazione**: **Loki**, **Barchetta**, **Slitta** oppure **Nessuna** (predefinita). Con **Dimensione dell’animazione › Doppia ×2** l’animazione scelta diventa grande il doppio.

- **Loki**: un gatto bianco e nero che fa quello che vuole: cammina, si ferma, si siede, si lecca una zampa, si sdraia a dormire, ogni tanto esce dallo schermo e poi torna.
- **Barchetta**: una nave a remi che attraversa lentamente un mare largo quanto il documento, poi sparisce per un po’ e riparte da sinistra.
- **Slitta**: Babbo Natale sulla sua slitta, tirata da due renne (la prima ha il naso rosso), corre sulla neve da sinistra a destra, poi sparisce e ritorna. Scegliendo il tema **Natale** parte da sola; lasciando il tema torna l’animazione di prima (se nel frattempo non l’hai cambiata a mano).

L’animazione non intralcia: non si può cliccare, passa sotto i pannelli, si nasconde in **Modifica** (dove c’è la barra di formattazione) e non compare nel PDF. Si ferma quando la scheda non è visibile e, se nel sistema è attiva la riduzione del movimento, resta ferma (il gatto dorme, la barca è in mezzo al mare).

## Anteprima immagine

Un clic su un’immagine in **Lettura** (o nell’elenco dei file) apre l’anteprima, con lo stesso zoom dell’editor immagini: all’apertura l’immagine è adattata alla finestra e la percentuale indica la grandezza reale (100% = un pixel dell’immagine per pixel dello schermo, fino all’800%).

- `Ctrl/⌘` + rotella o pinch sul trackpad ingrandisce sotto il puntatore; la rotella da sola sposta l’immagine ingrandita, come il trascinamento.
- I pulsanti − e + in basso, `Ctrl/⌘ + 0` per adattare alla finestra e `Ctrl/⌘ + 1` per il 100%; un clic sulla percentuale passa da una all’altra.
- **Doppio clic** sull’immagine: 100% sul punto cliccato, o di nuovo adattata.

## Modifica immagine

Per annotare un’immagine PNG, JPEG o WebP statica, aprila e scegli **Modifica immagine**, oppure, in **Modifica**, fai **doppio clic** sull’immagine nel documento. Un clic solo la seleziona: compaiono la maniglia per ridimensionarla e il pulsante **Modifica**. Con l’immagine selezionata, `Ctrl/⌘ + C` la **copia** (si incolla anche in Word, Paint o nella posta; incollata in Itaca diventa un riferimento allo stesso file, senza doppioni), `Ctrl/⌘ + X` la **taglia**, `Canc` o `Backspace` la **eliminano** (`Ctrl/⌘ + Z` la rimette) ed `Esc` toglie la selezione.

- **Strumenti**: penna (`P`), evidenziatore (`H`), gomma (`E`), linea (`L`), freccia (`A`), rettangolo (`R`), ellisse (`O`), testo (`T`) e ritaglio (`C`).
- **Stile**: colori rapidi o un colore a scelta, forme piene (`F`), spessore o dimensione del testo (`[` e `]`). Lo spessore iniziale si adatta alla grandezza dell’immagine.
- Tieni premuto **Maiusc** per tracciare linee e frecce orizzontali, verticali o a 45°, quadrati e cerchi.
- **Ritaglio**: trascina per scegliere l’area, poi spostala o allargala dagli angoli. Premi **Invio** per applicarlo ed **Esc** per annullarlo.
- **Rotazione** di 90° a sinistra o a destra, **Annulla** (`Ctrl+Z`) e **Ripeti** (`Ctrl+Y`).
- **Testo**: fai clic sull’immagine e scrivi direttamente lì. Colore e dimensione si possono cambiare mentre scrivi; `Esc` o un clic fuori confermano.
- **Zoom**: `Ctrl` + rotella o pinch sul trackpad, i pulsanti − e + in basso, `Ctrl+0` per adattare alla finestra e `Ctrl+1` per il 100%. Per spostarti tieni premuto **Spazio** e trascina, oppure usa la rotella.
- **Nome del file**: fai clic sul nome in alto per rinominare l’immagine (l’estensione resta invariata). Al salvataggio Itaca aggiorna tutti i documenti che la usano e sposta con lei la copia originale. `Invio` salva, `Esc` ripristina il nome.
- **Salva** (`Ctrl+S`) sostituisce il file ed è attivo solo dopo una modifica. Il primo salvataggio conserva l’originale in `.itaca-backup`, nella cartella dell’immagine: **Ripristina originale** lo recupera ed è attivo solo se il file è diverso dall’originale.

## Impostazioni

Al primo avvio: nessuna animazione, tema automatico, barra laterale a sinistra, documenti aperti in lettura, pannelli come descritto in **Spostare i pannelli**.

**Ripristina predefinite**, in basso a sinistra nella finestra, riporta tutte le impostazioni (aspetto, pannelli, documenti, file, PDF) a quelle del primo avvio, dopo una conferma. Restano la cartella di lavoro, le cartelle salvate, i percorsi delle cartelle, il tuo nome e i documenti.

Apri **Impostazioni** dall’icona in basso a destra, accanto al pulsante del tema, oppure con `Ctrl+,` (`Cmd+,` su Mac). Si chiude con **Esc**, con la **×** o con un clic fuori dalla finestra. Le sezioni sono a sinistra; ogni riga ha a destra il suo comando (interruttore, scelta o menu) e le opzioni compaiono solo quando servono, per esempio l’angolo solo se il riquadro sta nel documento. Le scelte restano salvate nel browser.

- **Aspetto**: tema (Laguna, Salvia, Terracotta, Indaco, Oceano, Ambra, Prugna, Rosa antico, Ardesia ognuno chiaro e scuro, e lo speciale **Natale**, sempre scuro: verde abete, rosso e la neve che cade nella barra laterale e si accumula in fondo, fino a un certo punto; il cumulo riparte da zero a ogni avvio o quando si torna al tema), modalità automatica/chiara/scura, dimensione del testo (80–140%), carattere del documento (con grazie, senza grazie, monospaziato), larghezza della colonna (stretta, media, larga, piena), **animazione** in fondo al documento (Loki, barchetta, slitta di Babbo Natale o nessuna, normale o doppia), **barra laterale** a sinistra o a destra (`Ctrl+Maiusc+B`, `Cmd+Maiusc+B` su Mac, la mostra o la nasconde) e **Marchio**: dimensione del logo (normale, grande, più grande; solo il logo oppure logo e titolo) e posizione della versione (accanto al nome, sotto il nome, in basso nella barra di stato, oppure nascosta).
- **Pannelli**: **Indice del documento**, **Citato da** e **Grafo dei collegamenti** si accendono e spengono uno per uno; indice e citazioni si mettono insieme nella barra laterale o in un angolo del documento, il grafo nella barra laterale o nel documento (nello stesso angolo di indice e citazioni se anche loro sono nel documento). **Ordine** decide chi sta sopra. Si possono anche trascinare, vedi **Spostare i pannelli**. L’indice evidenzia la sezione che stai leggendo.
- **Documenti**: come si apre un documento (lettura, modifica o sorgente Markdown), **Più documenti aperti** (uno, schede o affiancati: vedi **Più documenti aperti**), **Markdown mentre scrivi** (acceso all’inizio) e **Chiudi automaticamente** (spento all'inizio), vedi **Scrivere in Markdown**, e salvataggio automatico dopo una pausa di 2 s, 5 s, 15 s o 1 minuto. Il salvataggio automatico vale per i documenti già presenti sul disco. I documenti nuovi, quelli con immagini incollate non ancora salvate e quelli con sintassi avanzata si salvano ancora con **Salva**.
- **File**: conferma dell’eliminazione (conferma e nome digitato, oppure solo conferma), preselezione di «Aggiorna i collegamenti» quando rinomini o sposti (vale anche per gli spostamenti trascinando), **Documento iniziale** (vedi **Avvio**), **Inserimento rapido** (il varco con il **+** tra due voci dell’elenco, spento all’inizio), il tuo nome, mostrato agli altri quando stai modificando un documento (se non l’hai mai scritto, Itaca lo ricava dall’utente del computer quando lo trova nel percorso della cartella; altrimenti resta vuoto), e **Icona di Itaca** (vedi sotto).
- **PDF**: intestazione, piè di pagina e se mostrare le opzioni a ogni esportazione. Il PDF usa sempre i colori chiari della tavolozza scelta, anche quando lavori con il tema scuro.
- **Aggiornamenti**: la versione che usi, **Controlla ora**, le novità dell’ultima versione e se cercare gli aggiornamenti **all’avvio** (all’inizio) o **solo a mano** (vedi **Aggiornamenti**).

I menu a tendina (stile del paragrafo, Blocchi, Stili, scelte nelle finestre) usano la grafica di Itaca nei colori del tema invece del menu di sistema; sui dispositivi touch resta il selettore di sistema.

La versione di Itaca compare in una piccola etichetta accanto al nome, in alto nella barra laterale (oppure sotto il nome, in basso nella barra di stato o da nessuna parte, a scelta in **Impostazioni › Aspetto › Marchio**), e nella finestra Impostazioni. Il marchio è una colonna ionica che prende il colore della tavolozza e del tema; nella scheda del browser l’icona è la stessa colonna, bianca con il contorno nero, leggibile su qualsiasi sfondo.

## Glossario

L’icona del libro in basso a destra, accanto a **Impostazioni**, apre il **Glossario** (anche con `Ctrl+/`, `Cmd+/` su Mac). Si chiude con **Esc**, con la **×** o con un clic fuori.

- **Scorciatoie**: tutte le scorciatoie da tastiera.
- **Markdown**: come scrivere titoli, enfasi, elenchi, liste di controllo, citazioni, collegamenti (anche wiki), immagini, allegati, tabelle e codice.
- **Material per MkDocs**: le estensioni che Itaca mostra e conserva, come ammonimenti, riquadri espandibili, schede, griglie, didascalie, opzioni dei blocchi di codice, diagrammi Mermaid, formule, evidenziato e tasti, icone ed emoji, CriticMarkup, note a piè di pagina, annotazioni, abbreviazioni, elenchi di definizioni e attributi.

Ogni voce ha un esempio da copiare con un clic.

## Finestre di conferma

Nelle finestre con un campo da compilare (rinomina, nuovo documento, collegamento…) **Invio** conferma come il pulsante principale.

## Icona di Itaca

Il marchio di Itaca è una colonna ionica. In **Impostazioni › File › Icona di Itaca** puoi scaricarla per dare un’icona al file `Itaca Lite.html`; dopo il download compaiono le istruzioni.

- **Mac · PNG**: seleziona `Itaca Lite.html` nel Finder e premi `Cmd+I`; apri l’immagine scaricata, copiala (`Cmd+A`, `Cmd+C`), clicca l’icona piccola in alto nella finestra Informazioni e incolla (`Cmd+V`).
- **Windows · ICO**: Windows non permette di dare un’icona a un singolo file `.html`, quindi si usa un collegamento: tasto destro su `Itaca Lite.html` › *Mostra altre opzioni* › *Crea collegamento*, poi tasto destro sul collegamento › *Proprietà* › *Cambia icona…* › *Sfoglia* e scegli il file `.ico`.

L’icona va rimessa ogni volta che sostituisci il file con una nuova versione, anche quando Itaca si aggiorna da sola.

## Aggiornamenti

Le nuove versioni di Itaca sono pubblicate su GitHub, nelle [Release di eleamsi/itaca-lite](https://github.com/eleamsi/itaca-lite/releases).

- **Controllo**: all’apertura Itaca chiede a GitHub, una volta e in background, qual è l’ultima versione. In **Impostazioni › Aggiornamenti** puoi controllare quando vuoi con **Controlla ora** e scegliere **Solo a mano**: allora all’avvio Itaca non contatta GitHub.
- **Se c’è una versione nuova**: la pillola della versione diventa colorata con una freccia (clic = dettagli), sull’icona delle **Impostazioni** e sulla scheda **Aggiornamenti** compare un pallino, e in basso a destra un avviso con **Aggiorna** e **Novità** resta finché non lo chiudi con la **×** (per quella versione non torna; pillola e pallino restano). In **Impostazioni › Aggiornamenti** ci sono le novità della versione.
- **Aggiorna** (Chrome, Edge): Itaca chiede di salvare i documenti modificati, scarica il nuovo file da GitHub, controlla che sia completo e della versione giusta, lo scrive al posto del proprio file e si ricarica. Impostazioni, cartelle e schede restano. Se la cartella aperta è quella che contiene Itaca non chiede altro; altrimenti la prima volta ti chiede di scegliere il file `Itaca Lite.html` che stai usando (e se puoi modificarlo), poi se lo ricorda. Se qualcosa va storto il file non cambia.
- **Torna alla versione precedente**: la versione sostituita resta salvata nel browser; in **Impostazioni › Aggiornamenti** c’è **Torna alla X.Y.Z**.
- **Novità delle versioni**: le note di ogni versione sono dentro il file di Itaca, quindi si leggono anche senza connessione e senza andare su GitHub. Si aprono con un clic sulla pillola della versione accanto al nome (o in basso), oppure da **Impostazioni › Aggiornamenti › Novità delle versioni**: a sinistra l’elenco delle versioni con la data, a destra cosa è cambiato. Dopo un aggiornamento un avviso in basso a destra propone le novità, e le versioni che non avevi ancora visto sono segnate **nuova**.
- **Safari e Firefox** (e Itaca aperta da un server web): il browser non può modificare file sul disco, quindi **Aggiorna** scarica il nuovo `Itaca Lite.html` nella cartella Download e spiega come metterlo al posto di quello che usi.

## Segnalazioni

Il pulsante con il fumetto nella barra in basso apre **Segnalazioni**: un problema, un’idea per una nuova funzionalità o una domanda su Itaca.

- **Nuova**: scegli il tipo (**Problema**, **Funzionalità**, **Altro**), scrivi un titolo e una descrizione e premi **Invia** (o `Ctrl/⌘ + Invio` nella descrizione). Si apre su GitHub la segnalazione già compilata: premi **Create** per inviarla (serve un account GitHub gratuito). Con **Includi versione e browser** il testo riporta anche versione di Itaca, browser e sistema operativo; non vengono mai inviati nomi di cartelle, documenti o percorsi.
- **Le mie**: tutte le segnalazioni inviate da questo browser, con la versione di Itaca da cui le hai mandate e lo **stato** ben visibile: *Da confermare su GitHub* (non hai ancora premuto Create), *Ricevuta*, *In lavorazione*, *Risolta nella X.Y.Z*, *Non prevista* o *Doppione*, più il numero di risposte e il collegamento alla discussione. Se una segnalazione è risolta in una versione più nuova della tua, c’è il collegamento agli **Aggiornamenti**.
- Lo stato si aggiorna aprendo **Le mie**, con **Aggiorna stato** e, se cerchi gli aggiornamenti all’avvio, anche all’apertura di Itaca. Quando cambia, il pulsante delle segnalazioni ha un pallino e la segnalazione è segnata come **Novità**.

## Esportare in Word

**⋯ › Esporta in Word…** salva il documento come file **.docx**, da mandare a chi non usa Itaca o a chi chiede «il Word». Si sceglie dove salvarlo (in Safari e Firefox finisce nella cartella Download). Esporta quello che vedi, anche le modifiche non ancora salvate.

Il file usa gli stili veri di Word, quindi resta comodo da modificare: i titoli sono **Titolo 1–6** (compaiono nel riquadro di spostamento e in un sommario), gli elenchi sono elenchi puntati e numerati di Word, le tabelle hanno l’intestazione che si ripete su ogni pagina e i collegamenti a una sezione del documento portano a quel titolo. Le **note a piè di pagina** diventano note di Word, le **caselle** ☐/☒, le **immagini** sono incorporate (alla larghezza scelta, mai oltre la pagina) e i diagrammi Mermaid diventano immagini. Riquadri (avvisi, note, suggerimenti), citazioni e blocchi di codice stanno in un riquadro colorato; il codice mantiene i colori della sintassi. Le schede (`===`) diventano titoletti seguiti dal loro contenuto e le sezioni espandibili sono aperte. Pagina A4 con margini di 2 cm e numero di pagina in basso.

PDF e file incorporati diventano una riga con il loro nome (un link se sono su Internet); i collegamenti ad altri documenti della cartella restano testo, perché chi riceve il file non ha la cartella. Pages e l’anteprima del Mac mostrano riquadri e tabelle più stretti di come li disegna Word.

## Versioni e confronto con git

Se la cartella aperta è un repository git (contiene la cartella `.git`), Itaca legge la cronologia da sola, senza programmi esterni: serve quando una procedura cambia e bisogna capire cosa è stato modificato, da chi e quando.

- **⋯ › Versioni e confronto…** apre le versioni del documento. A sinistra c’è la **linea del tempo a nodi**: ogni punto è un commit che ha cambiato il documento, dal più recente; le linee colorate mostrano i rami (un ramo laterale che si riunisce è una modifica fatta in parallelo), i punti cerchiati le unioni, le etichette i rami e i tag. In cima, con il punto tratteggiato, le **modifiche non ancora registrate** (nell’editor o sul disco).
- **Confronto**: il documento disegnato com’è, con il testo **aggiunto in verde** e quello **tolto in rosso barrato**; una barretta a sinistra segna ogni punto cambiato (grigia se è cambiata solo la formattazione). **↑ ↓** saltano da una modifica all’altra, **Solo le modifiche** nasconde le parti uguali lasciando i titoli. Si confronta la versione scelta con quella da cui deriva (cioè: cosa ha cambiato quel commit); per **confrontare due versioni qualsiasi** scegli la prima nell’elenco e premi il pulsante **Confronta** (l’icona che compare a destra della seconda passandoci sopra): quella versione prende il bordo rosso «confronto» e il testo va dalla più vecchia (rosso) alla più nuova (verde). Premendolo di nuovo si torna alla precedente. Lo stesso si fa dal menu **con** (anche con il testo di adesso) o con **Maiusc + clic** sulla versione.
- **Markdown**: le righe del file cambiate, con i numeri di riga e le parole modificate evidenziate; «mostra» apre le righe uguali nascoste.
- **Autori** (*chi ha cambiato questa riga*): ogni riga con chi l’ha scritta o cambiata per ultimo, la data e il messaggio del commit; il colore è più pieno per le modifiche recenti. Le righe arrivate da un ramo unito sono attribuite a chi le ha scritte nel ramo. Un clic sull’autore mostra il confronto di quella modifica. **⋯ › Chi ha modificato questo punto…** apre direttamente gli Autori con evidenziata la riga dove si trova il cursore.
- **Anteprima**: la versione com’era. **Ripristina nell’editor** la mette nell’editor (il file cambia solo premendo Salva).
- **Tutta la cartella** (anche da **Cartelle e file › Storico git della cartella…**): il grafo di tutti i commit del repository con rami, unioni ed etichette. Un clic su un commit mostra messaggio, autore, data e i **file cambiati** (nuovi, modificati, eliminati): aprendo un file si vede il confronto (per i documenti come nel Confronto, per gli altri file di testo riga per riga, per le immagini prima e dopo affiancate). **Versioni** passa alla cronologia di quel documento, **Apri** lo apre.

Itaca legge il repository e non lo modifica: commit, rami e push si fanno con git o con il programma che usi di solito.

## Modifica condivisa

Quando passi a **Modifica** o **Markdown** su un documento della cartella, Itaca lo segnala con un piccolo file in `.itaca-locks`, rinnovato ogni 30 secondi e rimosso quando smetti di modificare o chiudi la pagina. Chi apre lo stesso documento da un’altra scheda o da un altro computer che usa la stessa cartella (per esempio una cartella di rete o sincronizzata) lo vede in sola lettura, con l’indicazione **In modifica: nome**.

- Il documento resta leggibile; la modifica si sblocca da sola quando l’altro utente ha finito.
- Se Itaca si è chiusa senza rilasciare il documento, il blocco scade dopo circa 2 minuti e mezzo. Puoi anche premere **In modifica: nome** e scegliere **Modifica comunque**: l’altro utente passa in sola lettura (se ha modifiche non salvate riceve un avviso).
- Con le cartelle sincronizzate nel cloud il blocco arriva agli altri con il ritardo della sincronizzazione.

## Versioni

La prima versione è **1.0.0**, contrassegnata dal tag Git `v1.0.0`. Le versioni successive seguiranno lo schema `MAJOR.MINOR.PATCH`.

La versione corrente è indicata nel file HTML, nel tag `<meta name="version">`: aggiornala a ogni rilascio insieme al tag Git. Ogni versione ha anche una **Release** su GitHub con le novità e il file `Itaca-Lite-X.Y.Z.zip`, che contiene `Itaca Lite.html`: è da lì che Itaca legge gli aggiornamenti. Il file è dentro uno ZIP perché GitHub non accetta spazi nei nomi degli allegati e scaricato direttamente diventerebbe `Itaca.Lite.html`.
