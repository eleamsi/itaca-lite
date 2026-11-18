# Itaca Lite

Itaca Lite è un editor Markdown locale in un unico file HTML. Offre una modalità visuale e una sorgente Markdown, supporta le estensioni di Material for MkDocs e permette di esportare i documenti in PDF o la cartella in un sito HTML statico.

## Avvio

1. Scarica `Itaca Lite.html` e aprilo in Chrome o Edge.
2. Al primo avvio usa **Scegli cartella** per selezionare la cartella dei documenti `.md` (di solito quella che contiene Itaca) e consenti la modifica dei file: il browser chiede un solo permesso, valido per lettura e scrittura.
   Agli avvii successivi Itaca riapre da sola l’ultima cartella. Se il browser ha dimenticato il permesso, basta un clic o un tasto qualsiasi per concederlo di nuovo; scegli **Consenti a ogni visita**, se il browser lo propone, per non doverlo più ripetere.
3. Seleziona un documento dalla barra laterale.

## Ricerca nei documenti

La casella **Cerca nei documenti…** in alto nella barra laterale (`Ctrl/⌘ + K`) cerca nei nomi, nelle cartelle e nel testo di tutti i documenti della cartella.

- Non distingue maiuscole e accenti: `perche` trova anche «Perché». Più parole devono esserci tutte; per una frase esatta usa le virgolette (`"motore principale"`).
- Ogni risultato mostra la sezione in cui si trova (§ titolo), quante volte compare e un estratto. Clic sul risultato per aprirlo sulla prima occorrenza; clic di nuovo per passare alla successiva.
- Tastiera: **Invio** apre il primo risultato, **↓/↑** scorrono i risultati, **Esc** torna alla casella o la svuota.
- I file cambiati fuori da Itaca (da un altro programma o da un altro utente) vengono riletti alla ricerca successiva.

## Barra di formattazione

Compare in basso quando sei in **Modifica**. I comandi delle tabelle (righe, colonne, allineamento) compaiono solo con il cursore in una tabella; **Blocchi** contiene riquadro, sezione espandibile e i blocchi Material for MkDocs. Sugli schermi stretti la barra è una sola riga che scorre in orizzontale, con il bordo sfumato dove ci sono altri comandi.

## Modifiche non salvate

Se cambi documento, ricarichi o apri un’altra cartella con modifiche non salvate, Itaca chiede **Salvare le modifiche?**: **Salva** (o `Invio`) salva e prosegue, **Non salvare** scarta le modifiche, **Annulla** (o `Esc`) resta sul documento.

## Barra del documento

In alto a destra, da sinistra a destra:

- **Lettura · Modifica · Markdown**: come vedi il documento. In **Lettura** non si può modificare; **Modifica** apre l’editor visuale con la barra di formattazione; **Markdown** modifica il sorgente. Nelle finestre strette restano solo le icone.
- **Cerca** (`Ctrl/⌘ + H`): trova e sostituisci nel documento.
- **⋯ Altre azioni**: **Esporta PDF…** e, se la cartella è un repository git, **Versioni precedenti…**.
- **Salva** (`Ctrl/⌘ + S`): compare quando modifichi o quando ci sono modifiche non salvate.

## Modifica immagine

Per annotare un’immagine PNG, JPEG o WebP statica, aprila e scegli **Modifica immagine**.

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

Apri **Impostazioni** dall’icona in basso a destra, accanto al pulsante del tema, oppure con `Ctrl+,` (`Cmd+,` su Mac). Le scelte restano salvate nel browser.

- **Aspetto**: tema (Laguna, Salvia, Terracotta o Indaco, ognuno chiaro e scuro), modalità automatica/chiara/scura, dimensione del testo (80–140%), carattere del documento (con grazie, senza grazie, monospaziato), larghezza della colonna (stretta, media, larga, piena) e posizione di **Indice del documento** e **Citato da**: nella barra laterale oppure a lato del documento, in alto a destra, sempre visibili mentre scorri (nelle finestre strette tornano nella barra laterale). L’indice evidenzia la sezione che stai leggendo.
- **Documenti**: come si apre un documento (lettura, modifica o sorgente Markdown) e salvataggio automatico dopo una pausa di 2 s, 5 s, 15 s o 1 minuto. Il salvataggio automatico vale per i documenti già presenti sul disco. I documenti nuovi, quelli con immagini incollate non ancora salvate e quelli con sintassi avanzata si salvano ancora con **Salva**.
- **File**: conferma dell’eliminazione (conferma e nome digitato, oppure solo conferma), preselezione di «Aggiorna i collegamenti» quando rinomini o sposti e il tuo nome, mostrato agli altri quando stai modificando un documento.
- **PDF**: intestazione, piè di pagina e se mostrare le opzioni a ogni esportazione.

La versione di Itaca compare sotto il nome, in alto nella barra laterale, e nella finestra Impostazioni.

## Modifica condivisa

Quando passi a **Modifica** o **Markdown** su un documento della cartella, Itaca lo segnala con un piccolo file in `.itaca-locks`, rinnovato ogni 30 secondi e rimosso quando smetti di modificare o chiudi la pagina. Chi apre lo stesso documento da un’altra scheda o da un altro computer che usa la stessa cartella (per esempio una cartella di rete o sincronizzata) lo vede in sola lettura, con l’indicazione **In modifica: nome**.

- Il documento resta leggibile; la modifica si sblocca da sola quando l’altro utente ha finito.
- Se Itaca si è chiusa senza rilasciare il documento, il blocco scade dopo circa 2 minuti e mezzo. Puoi anche premere **In modifica: nome** e scegliere **Modifica comunque**: l’altro utente passa in sola lettura (se ha modifiche non salvate riceve un avviso).
- Con le cartelle sincronizzate nel cloud il blocco arriva agli altri con il ritardo della sincronizzazione.

## Versioni

La prima versione è **1.0.0**, contrassegnata dal tag Git `v1.0.0`. Le versioni successive seguiranno lo schema `MAJOR.MINOR.PATCH`.

La versione corrente è indicata nel file HTML, nel tag `<meta name="version">`: aggiornala a ogni rilascio insieme al tag Git.
