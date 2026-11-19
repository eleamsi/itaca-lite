# Itaca Lite

Itaca Lite è un editor Markdown locale in un unico file HTML. Offre una modalità visuale e una sorgente Markdown, supporta le estensioni di Material for MkDocs e permette di esportare i documenti in PDF o la cartella in un sito HTML statico.

## Avvio

1. Scarica `Itaca Lite.html` e aprilo in Chrome o Edge.
2. Al primo avvio usa **Scegli cartella** per selezionare la cartella dei documenti `.md` (di solito quella che contiene Itaca) e consenti la modifica dei file: il browser chiede un solo permesso, valido per lettura e scrittura.
   Agli avvii successivi Itaca riapre da sola l’ultima cartella. Se il browser ha dimenticato il permesso, basta un clic o un tasto qualsiasi per concederlo di nuovo; scegli **Consenti a ogni visita**, se il browser lo propone, per non doverlo più ripetere.
3. Seleziona un documento dalla barra laterale.

## Nuovo documento

- **Nuovo documento** in alto nella barra laterale chiede la **Cartella** (proposta: quella del documento aperto) e il nome. Scrivendo `Sottocartella/Nome` crei anche la sottocartella.
- Per fare prima, passa con il mouse tra due voci dell’elenco: compare un **+** con una linea. Cliccalo, scrivi il nome e premi **Invio** (**Esc** annulla). Il documento va nella cartella della voce sopra, oppure dentro di essa se è una cartella aperta.
- Anche il menu **⋯** di una cartella o di un documento ha **Nuovo documento qui**.

**Copia percorso** nel menu **⋯** di un file o di una cartella, oppure l’icona accanto al percorso in basso, copia il percorso completo sul computer (per esempio `/Users/nome/Documenti/docs/Procedure/Guida.md`). Il browser non rivela dove si trova la cartella: se è quella che contiene Itaca lo ricava da solo, altrimenti te lo chiede la prima volta e lo ricorda. Puoi correggerlo in **Impostazioni › File › Percorso della cartella aperta**.

## Cartelle salvate

Se lavori spesso con le stesse cartelle, salvale per riaprirle senza cercarle ogni volta.

- Con una cartella aperta, premi la **stella** accanto al suo nome in cima all’elenco. La stella piena indica che è già salvata; premila di nuovo per toglierla.
- **Cartelle salvate**, in basso nella barra laterale, elenca le cartelle salvate: clic sul nome per aprirla. Passando sopra una voce compaiono **Modifica** (cambia il nome nell’elenco o, con **Cambia cartella…**, la cartella sul disco) e **×**, che la toglie dall’elenco senza toccare i file.
- Il browser può chiedere di nuovo il permesso quando apri una cartella salvata.

## Ricerca nei documenti

La casella **Cerca nei documenti…** in alto nella barra laterale (`Ctrl/⌘ + K`) cerca nei nomi, nelle cartelle e nel testo di tutti i documenti della cartella.

- Non distingue maiuscole e accenti: `perche` trova anche «Perché». Più parole devono esserci tutte; per una frase esatta usa le virgolette (`"motore principale"`).
- Ogni risultato mostra la sezione in cui si trova (§ titolo), quante volte compare e un estratto. Clic sul risultato per aprirlo sulla prima occorrenza; clic di nuovo per passare alla successiva.
- Tastiera: **Invio** apre il primo risultato, **↓/↑** scorrono i risultati, **Esc** torna alla casella o la svuota.
- I file cambiati fuori da Itaca (da un altro programma o da un altro utente) vengono riletti alla ricerca successiva.

## Barra di formattazione

Compare in basso quando sei in **Modifica**. I comandi delle tabelle (righe, colonne, allineamento) compaiono solo con il cursore in una tabella; **Blocchi** contiene riquadro, sezione espandibile e i blocchi Material for MkDocs. Sugli schermi stretti la barra è una sola riga che scorre in orizzontale, con il bordo sfumato dove ci sono altri comandi.

## Collegamenti

In **Lettura**, passando sopra un collegamento a un documento ne vedi l’anteprima; in **Modifica** l’anteprima non compare. In **Modifica**, con il cursore dentro un collegamento compare un piccolo riquadro con la destinazione e tre pulsanti: **Apri**, **Modifica** (testo, documento interno o URL) e **Rimuovi**, che lascia il testo senza collegamento (`Ctrl/⌘ + Z` lo ripristina). Anche il pulsante 🔗 della barra di formattazione modifica il collegamento in cui si trova il cursore, invece di crearne uno nuovo.

## Allegati

Oltre alle immagini puoi inserire file di qualsiasi tipo (PDF, Word, Excel, archivi…): **incollali** dopo averli copiati dal Finder o da Esplora risorse, **trascinali** nel punto del testo che vuoi, oppure usa il pulsante 📎 della barra di formattazione. Nel testo compare un collegamento con il nome del file; al salvataggio il file viene copiato in `_allegati` (se il nome è già usato diventa «Nome (2).pdf»).

Aprendo il collegamento (clic in **Lettura**, **Apri** nel riquadro del collegamento in **Modifica**) PDF, testi, audio e video si aprono in una nuova scheda; gli altri file vengono scaricati.

## Modifiche non salvate

Se cambi documento, ricarichi o apri un’altra cartella con modifiche non salvate, Itaca chiede **Salvare le modifiche?**: **Salva** (o `Invio`) salva e prosegue, **Non salvare** scarta le modifiche, **Annulla** (o `Esc`) resta sul documento.

## Barra del documento

In alto a destra, da sinistra a destra:

- **Lettura · Modifica · Markdown**: come vedi il documento. In **Lettura** non si può modificare; **Modifica** apre l’editor visuale con la barra di formattazione; **Markdown** modifica il sorgente. Nelle finestre strette restano solo le icone.
- **Cerca** (`Ctrl/⌘ + H`): trova e sostituisci nel documento.
- **⋯ Altre azioni**: **Esporta PDF…** e, se la cartella è un repository git, **Versioni precedenti…**.
- **Salva** (`Ctrl/⌘ + S`): compare quando modifichi o quando ci sono modifiche non salvate.

## Modifica immagine

Per annotare un’immagine PNG, JPEG o WebP statica, aprila e scegli **Modifica immagine**, oppure, in **Modifica**, fai clic sull’immagine nel documento: si apre subito l’editor e, alla chiusura, l’immagine resta selezionata per ridimensionarla.

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

- **Aspetto**: tema (Laguna, Salvia, Terracotta o Indaco, ognuno chiaro e scuro), modalità automatica/chiara/scura, dimensione del testo (80–140%), carattere del documento (con grazie, senza grazie, monospaziato), larghezza della colonna (stretta, media, larga, piena), **barra laterale** a sinistra o a destra (`Ctrl+Maiusc+B`, `Cmd+Maiusc+B` su Mac, la mostra o la nasconde) e **Indice del documento** e **Citato da**: si possono nascondere uno per uno e mettere nella barra laterale oppure nel documento, in uno dei quattro angoli, sempre visibili mentre scorri (nelle finestre strette tornano nella barra laterale). L’indice evidenzia la sezione che stai leggendo.
- **Documenti**: come si apre un documento (lettura, modifica o sorgente Markdown) e salvataggio automatico dopo una pausa di 2 s, 5 s, 15 s o 1 minuto. Il salvataggio automatico vale per i documenti già presenti sul disco. I documenti nuovi, quelli con immagini incollate non ancora salvate e quelli con sintassi avanzata si salvano ancora con **Salva**.
- **File**: conferma dell’eliminazione (conferma e nome digitato, oppure solo conferma), preselezione di «Aggiorna i collegamenti» quando rinomini o sposti e il tuo nome, mostrato agli altri quando stai modificando un documento.
- **PDF**: intestazione, piè di pagina e se mostrare le opzioni a ogni esportazione.
- **Scorciatoie**: elenco delle scorciatoie da tastiera disponibili (per ora non modificabili).

I menu a tendina (stile del paragrafo, Blocchi, Stili, scelte nelle finestre) usano la grafica di Itaca nei colori del tema invece del menu di sistema; sui dispositivi touch resta il selettore di sistema.

La versione di Itaca compare sotto il nome, in alto nella barra laterale, e nella finestra Impostazioni.

## Modifica condivisa

Quando passi a **Modifica** o **Markdown** su un documento della cartella, Itaca lo segnala con un piccolo file in `.itaca-locks`, rinnovato ogni 30 secondi e rimosso quando smetti di modificare o chiudi la pagina. Chi apre lo stesso documento da un’altra scheda o da un altro computer che usa la stessa cartella (per esempio una cartella di rete o sincronizzata) lo vede in sola lettura, con l’indicazione **In modifica: nome**.

- Il documento resta leggibile; la modifica si sblocca da sola quando l’altro utente ha finito.
- Se Itaca si è chiusa senza rilasciare il documento, il blocco scade dopo circa 2 minuti e mezzo. Puoi anche premere **In modifica: nome** e scegliere **Modifica comunque**: l’altro utente passa in sola lettura (se ha modifiche non salvate riceve un avviso).
- Con le cartelle sincronizzate nel cloud il blocco arriva agli altri con il ritardo della sincronizzazione.

## Versioni

La prima versione è **1.0.0**, contrassegnata dal tag Git `v1.0.0`. Le versioni successive seguiranno lo schema `MAJOR.MINOR.PATCH`.

La versione corrente è indicata nel file HTML, nel tag `<meta name="version">`: aggiornala a ogni rilascio insieme al tag Git.
