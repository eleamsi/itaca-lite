"""Note della finestra «Novità» di Itaca Lite.

Le note stanno nell'HTML, nel blocco
<script type="application/json" id="itacaChangelog">: [{version, date, notes}, …],
dalla più recente. Questo script lo legge e lo riscrive; non serve altro.

    python build.py estrai      scrive X.Y.Z.md e dates.txt da quello che c'è nell'HTML
    python build.py             rimette nell'HTML le note di ogni X.Y.Z.md (nuove o
                                cambiate) con la data di dates.txt (oggi se manca)
    python build.py controlla   rilegge e riscrive senza cambiare nulla: il file deve
                                restare identico byte per byte

X.Y.Z.md = stesso testo della Release su GitHub, senza «Come aggiornare».
dates.txt = una riga «X.Y.Z AAAA-MM-GG» per versione.
"""
import datetime
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
HTML = HERE.parent.parent / 'Itaca Lite.html'
BLOCK = re.compile(r'(<script type="application/json" id="itacaChangelog">)(.*?)(</script>)', re.S)
VERSION = re.compile(r'^\d+\.\d+\.\d+$')


def key(version):
    return tuple(int(part) for part in version.split('.'))


def load():
    text = HTML.read_bytes().decode('utf-8')
    match = BLOCK.search(text)
    if not match:
        sys.exit('Blocco itacaChangelog non trovato in ' + str(HTML))
    return text, match, json.loads(match.group(2))


def save(text, match, entries):
    entries.sort(key=lambda entry: key(entry['version']), reverse=True)
    data = json.dumps(entries, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    result = text[:match.start(2)] + data + text[match.end(2):]
    if result != text:
        HTML.write_bytes(result.encode('utf-8'))
    return result != text


def dates():
    found = {}
    path = HERE / 'dates.txt'
    if path.exists():
        for line in path.read_text(encoding='utf-8').splitlines():
            parts = line.split()
            if len(parts) >= 2 and VERSION.match(parts[0]):
                found[parts[0]] = parts[1]
    return found


def extract():
    _, _, entries = load()
    for entry in entries:
        (HERE / (entry['version'] + '.md')).write_bytes((entry['notes'] + '\n').encode('utf-8'))
    lines = sorted((entry['version'] + ' ' + entry['date'] for entry in entries), key=lambda line: key(line.split()[0]))
    (HERE / 'dates.txt').write_bytes(('\n'.join(lines) + '\n').encode('utf-8'))
    print(len(entries), 'versioni estratte in', HERE)


def build():
    text, match, entries = load()
    by_version = {entry['version']: entry for entry in entries}
    known = dates()
    today = datetime.date.today().isoformat()
    changed = []
    for path in HERE.glob('*.md'):
        version = path.stem
        if not VERSION.match(version):
            continue
        notes = path.read_bytes().decode('utf-8').replace('\r\n', '\n').strip()
        date = known.get(version) or by_version.get(version, {}).get('date') or today
        entry = by_version.get(version)
        if entry and entry['notes'] == notes and entry['date'] == date:
            continue
        if entry:
            entry.update(notes=notes, date=date)
        else:
            entry = {'version': version, 'date': date, 'notes': notes}
            entries.append(entry)
            by_version[version] = entry
        changed.append(version)
    save(text, match, entries)
    print('Aggiornate:', ', '.join(sorted(changed, key=key)) if changed else 'nessuna')


def check():
    text, match, entries = load()
    if save(text, match, entries):
        sys.exit('ATTENZIONE: riscrivendo il blocco il file è cambiato')
    print('OK:', len(entries), 'versioni, file invariato')


if __name__ == '__main__':
    command = sys.argv[1] if len(sys.argv) > 1 else 'build'
    {'estrai': extract, 'build': build, 'controlla': check}.get(command, build)()
