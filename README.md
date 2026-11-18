# Itaca Lite

Itaca Lite è un editor Markdown locale in un unico file HTML. Offre una modalità visuale e una sorgente Markdown, supporta le estensioni di Material for MkDocs e permette di esportare i documenti in PDF o la cartella in un sito HTML statico.

## Avvio

1. Scarica `Itaca Lite.html` e aprilo in Chrome o Edge.
2. Al primo avvio usa **Scegli cartella** per selezionare la cartella dei documenti `.md` (di solito quella che contiene Itaca) e consenti la modifica dei file: il browser chiede un solo permesso, valido per lettura e scrittura.
   Agli avvii successivi Itaca riapre da sola l’ultima cartella. Se il browser ha dimenticato il permesso, basta un clic o un tasto qualsiasi per concederlo di nuovo; scegli **Consenti a ogni visita**, se il browser lo propone, per non doverlo più ripetere.
3. Seleziona un documento dalla barra laterale. Per annotare o ritagliare un’immagine PNG, JPEG o WebP statica, apri **Modifica immagine**. Il primo salvataggio conserva l’originale in `.itaca-backup`, nella cartella dell’immagine. Usa **Ripristina originale** per recuperarlo.

## Impostazioni

Apri **Impostazioni** dall’icona in basso a destra, accanto al pulsante del tema, oppure con `Ctrl+,` (`Cmd+,` su Mac). Le scelte restano salvate nel browser.

- **Aspetto**: tema (Laguna, Salvia, Terracotta o Indaco, ognuno chiaro e scuro), modalità automatica/chiara/scura, dimensione del testo (80–140%), carattere del documento (con grazie, senza grazie, monospaziato) e larghezza della colonna (stretta, media, larga, piena).
- **Documenti**: come si apre un documento (lettura, modifica o sorgente Markdown) e salvataggio automatico dopo una pausa di 2 s, 5 s, 15 s o 1 minuto. Il salvataggio automatico vale per i documenti già presenti sul disco. I documenti nuovi, quelli con immagini incollate non ancora salvate e quelli con sintassi avanzata si salvano ancora con **Salva**.
- **File**: conferma dell’eliminazione (conferma e nome digitato, oppure solo conferma) e preselezione di «Aggiorna i collegamenti» quando rinomini o sposti.
- **PDF**: intestazione, piè di pagina e se mostrare le opzioni a ogni esportazione.

La versione di Itaca compare sotto il nome, in alto nella barra laterale, e nella finestra Impostazioni.

## Versioni

La prima versione è **1.0.0**, contrassegnata dal tag Git `v1.0.0`. Le versioni successive seguiranno lo schema `MAJOR.MINOR.PATCH`.

La versione corrente è indicata nel file HTML, nel tag `<meta name="version">`: aggiornala a ogni rilascio insieme al tag Git.
