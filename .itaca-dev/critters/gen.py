"""Generate pixel-art sprite sheets for Itaca Lite's cat, boat and Christmas sleigh.

Frames are ASCII grids; each colour letter becomes one <path> per sheet made of
horizontal runs, so the markup stays tiny. Output: sprites.html (markup only).
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

NAMES = {'K': 'k', 'k': 'k2', 'W': 'w', 'w': 'w2', 'P': 'p', 'G': 'g', 'e': 'e', 'Z': 'z', 'o': 'o',
         'M': 'm', 'S': 's', 's': 's2', 'T': 't', 'D': 't2', 'H': 'h', 'h': 'h2', '~': 'c', 'v': 'v'}
# boat greens use 'H'/'h' to avoid clashing with the cat's eye colour
# ---------------------------------------------------------------- helpers
def grid(rows, w):
    rows = [r.ljust(w, '.') for r in rows]
    assert all(len(r) == w for r in rows), [len(r) for r in rows]
    return [list(r) for r in rows]

def put(g, x, y, c):
    if 0 <= y < len(g) and 0 <= x < len(g[0]):
        g[y][x] = c

def copy(g):
    return [r[:] for r in g]

def outline(g, line='o', skip='Zw~'):
    """Add a 1px outline around every opaque pixel (not around `skip`)."""
    h, w = len(g), len(g[0])
    out = copy(g)
    for y in range(h):
        for x in range(w):
            if g[y][x] != '.':
                continue
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                xx, yy = x + dx, y + dy
                if 0 <= xx < w and 0 <= yy < h and g[yy][xx] not in '.' + skip:
                    out[y][x] = line
                    break
    return out

def pad(g, n=1):
    w = len(g[0]) + 2 * n
    blank = ['.'] * w
    return [blank[:] for _ in range(n)] + [['.'] * n + r + ['.'] * n for r in g] + [blank[:] for _ in range(n)]

def sheet(frames, cls, prefix):
    """frames: list of grids, same size. Returns an <svg> string, 1 unit = 1 pixel."""
    h, w = len(frames[0]), len(frames[0][0])
    paths = {}
    for i, f in enumerate(frames):
        for y, row in enumerate(f):
            x = 0
            while x < w:
                c = row[x]
                if c == '.':
                    x += 1
                    continue
                x0 = x
                while x < w and row[x] == c:
                    x += 1
                paths.setdefault(c, []).append(f'M{i * w + x0} {y}h{x - x0}v1h-{x - x0}z')
    body = ''.join(f'<path class="{prefix}{NAMES[c]}" d="{"".join(d)}"/>'
                   for c, d in sorted(paths.items()))
    n = len(frames)
    return (f'<svg class="sheet {cls}" viewBox="0 0 {w * n} {h}" width="{w * n}" height="{h}" '
            f'style="--n:{n}" shape-rendering="crispEdges" aria-hidden="true">{body}</svg>'), (w, h)

# ---------------------------------------------------------------- the cat
# K black fur, k far legs, W white, w far white legs (lower-case = class name
# doubled for capitals), P pink, G eyes, e closed eye, Z sleep letters.
W_CAT = 20

STAND_TOP = [
    "....................",
    "....................",
    "..K...........K....K",
    ".K............KKKKKK",
    ".K............KKKKKK",
    ".K............KGKKGK",
    "..K.KKKKKKKKKKKWPPWK",
    "...KKKKKKKKKKKKWWWW.",
    "...KKKKKKKKKKKWWWW..",
    "...KKKKKKKKKKWWWWW..",
    "....KKKWWWWWWWWWW...",
]

def stand(legs=(0, 0, 0, 0), tail=0):
    g = grid(STAND_TOP + ["", "", ""], W_CAT)
    if tail:  # tail tip sways one pixel
        put(g, 2, 2, '.'); put(g, 1, 2, 'K')
    hips = ((4, 'k', 'w'), (6, 'K', 'W'), (13, 'w', 'w'), (15, 'W', 'W'))
    # far legs first so near legs overlap them
    for (hip, leg, paw), dx in zip(hips, legs):
        put(g, hip, 11, leg)
        put(g, hip + dx, 12, leg)
        put(g, hip + dx, 13, paw)
    return g

WALK = [stand((1, -1, -1, 1)), stand((0, 0, 0, 0), 1), stand((-1, 1, 1, -1)), stand((0, 0, 0, 0))]
STAND = [stand()]

SIT_BASE = [
    "..........K....K....",
    "..........KKKKKK....",
    "..........KKKKKK....",
    "..........KGKKGK....",
    "..........KWPPWK....",
    "...........WWWW.....",
    ".........KKKWWW.....",
    "........KKKKWWW.....",
    ".......KKKKKWWW.....",
    "......KKKKKKKwW.....",
    ".....KKKKKKKKwW.....",
    ".....KKKKKKKKwW.....",
    ".....KKKKKKKWwW.....",
    ".KKKKKKKKKKWWwWW....",
]

def sit(tail=0, blink=False):
    g = grid(SIT_BASE, W_CAT)
    put(g, 1, 12, 'K')
    if tail >= 1:
        put(g, 1, 13, '.'); put(g, 1, 11, 'K')
    if tail >= 2:
        put(g, 1, 11, '.'); put(g, 0, 11, 'K'); put(g, 0, 10, 'K')
    if blink:
        put(g, 11, 3, 'e'); put(g, 14, 3, 'e')
    return g

IDLE = [sit(0), sit(0), sit(1), sit(2), sit(2), sit(1), sit(0), sit(0, True)]

def lick(stage):
    """0 = sitting, 1 = paw up, 2 = paw at mouth + tongue, 3 = paw at mouth."""
    g = sit(0, blink=stage >= 2)
    if stage == 0:
        return g
    for y in range(10, 14):
        put(g, 14, y, '.')
    put(g, 15, 13, '.')
    put(g, 13, 13, 'w')
    if stage == 1:
        for y in (9, 8):
            put(g, 15, y, 'W')
        put(g, 15, 7, 'W'); put(g, 16, 7, 'W')
    else:
        for y in (9, 8, 7):
            put(g, 15, y, 'W')
        put(g, 15, 6, 'W'); put(g, 16, 6, 'W')
        put(g, 16, 5, 'W')
        if stage == 2:
            put(g, 15, 5, 'P')
    return g

LICK = [lick(0), lick(1), lick(2), lick(3), lick(2), lick(3), lick(2), lick(1)]

SLEEP_BASE = [
    "", "", "", "", "", "", "",
    "......KKKKKK.K....K.",
    "....KKKKKKKKKKKKKKK.",
    "...KKKKKKKKKKKKKKKK.",
    "...KKKKKKKKKKKeKKeK.",
    "..KKKKKKKKKKKKWPPWK.",
    "..KKKKKKKKKKKWWWWW..",
    ".KKKKKKKKKKKKKKKK...",
]

Z = ["ZZZ", ".Z.", "ZZZ"]

def sleep(up=False, z=None):
    g = grid(SLEEP_BASE, W_CAT)
    if up:
        for x in range(7, 11):
            put(g, x, 6, 'K')
    if z is not None:
        zx, zy = z
        for dy, row in enumerate(Z):
            for dx, c in enumerate(row):
                if c != '.':
                    put(g, zx + dx, zy + dy, 'Z')
    return g

SLEEP = [sleep(), sleep(True, (16, 4)), sleep(True, (17, 1)), sleep()]

CROUCH = grid([
    "", "", "", "",
    "............K....K..",
    "............KKKKKK..",
    "......KKKKKKKKKKKK..",
    "....KKKKKKKKKeKKeK..",
    "...KKKKKKKKKKWPPWK..",
    "...KKKKKKKKKKWWWW...",
    "..KKKKKKKKKKKWWW....",
    "..KKKKKKKKKKKWWW....",
    "..KKKKKKKKKKWWWW....",
    ".KKKKKKKKKKKWWWWW...",
], W_CAT)

HALF_SIT = grid([
    "",
    "............K....K..",
    "............KKKKKK..",
    "............KKKKKK..",
    "............KGKKGK..",
    "........KKKKKWPPWK..",
    "......KKKKKK.WWWW...",
    "....KKKKKKKKWWWW....",
    "....KKKKKKKKWWW.....",
    "...KKKKKKKKKWWW.....",
    "...KKKKKKKKK.wW.....",
    "...KKKKKKKK..wW.....",
    "....KKKKKKK..wW.....",
    "..KKKKKKKWW..wW.....",
], W_CAT)

SIT_DOWN = [stand(), HALF_SIT, sit(0)]       # played backwards to stand up
LIE_DOWN = [sit(0), CROUCH, sleep()]          # played backwards to wake up

CAT_SHEETS = {
    'walk': WALK, 'stand': STAND, 'idle': IDLE, 'lick': LICK,
    'sleep': SLEEP, 'sit': SIT_DOWN, 'lie': LIE_DOWN,
}

# ---------------------------------------------------------------- the boat
W_BOAT = 28
BOAT = [
    "",
    ".............M..............",
    "........MMMMMMMMMMM.........",
    ".........SSSSMSSSSs.........",
    ".........SSSSMSSSSSs........",
    ".TTT......SSSMSSSSSs........",
    "T...T.....SSSMSSSSSs........",
    "T.TT......SSSMSSSSs.........",
    "T..........SSMSSSs......TTT.",
    ".T...........M...........T..",
    "..T..........M...........T..",
    "...TTTTTTTTTTTTTTTTTTTTTTT..",
    "...TTTTDTTTDTTTDTTTDTTDDDD..",
    "....HHHHHHHHHHHHHHHHHHHHHH..",
    ".....hhhhhhhhhhhhhhhhhhhhh..",
    "......hhhhhhhhhhhhhhhhhh....",
]
OAR_PORTS = (7, 11, 15, 19)

def boat(frame):
    g = grid(BOAT + ["", ""], W_BOAT)
    stroke = (frame // 2) % 2
    for x in OAR_PORTS:
        put(g, x, 12, 'M')
        pts = [(x, 13), (x - 1, 14), (x - 2, 15), (x - 3, 16), (x - 4, 16)] if stroke == 0 else \
              [(x, 13), (x, 14), (x - 1, 15), (x - 1, 16), (x - 2, 16)]
        for px, py in pts:
            put(g, px, py, 'M')
    g = outline(g, 'o')
    # rock: shear columns by -1/0/+1 pixel around the middle
    tilt = (0, 1, 1, 0, 0, -1, -1, 0)[frame]
    h, w = len(g), len(g[0])
    rocked = [['.'] * w for _ in range(h)]
    for x in range(w):
        dy = round(tilt * (x - (w - 1) / 2) / ((w - 1) / 2))
        for y in range(h):
            if g[y][x] != '.':
                put(rocked, x, y + dy, g[y][x])
    return rocked

# ---------------------------------------------------------------- the sea
# one 16 x 7 tile repeated across the whole width; c crest, L light, M mid, D deep
SEA = [
    "......cccc......",
    "....ccLLLLcc....",
    "ccccLLLLLLLLcccc",
    "LLLLLLLLLLLLLLLL",
    "MMMLLLMMMMMMMMMM",
    "MMMMMMMMMMMLLLMM",
    "DDDDDDDDDDDDDDDD",
]

BOAT_FRAMES = [boat(i) for i in range(8)]

# ---------------------------------------------------------------- the sleigh (Natale)
# Babbo Natale sulla slitta, tirata da due renne (la prima col naso rosso), verso destra.
# B renna, b zampe lontane, L pancia, A corna, N naso rosso, n naso scuro, E occhio,
# R rosso, r rosso scuro, Y oro, W bianco, F viso, K cintura, V sacco, q redini
W_SLEIGH, H_SLEIGH = 64, 19

REINDEER = [
    "......A.A.......",
    ".......AA.A.....",
    "........AAA.....",
    "..........A.....",
    "..........BBB...",
    "..........BEBBB.",
    "..........BBBBBn",
    ".........BBB....",
    "W.......BBBB....",
    "WBBBBBBBBBB.....",
    "BBBBBBBBBBB.....",
    ".BBBBBBBBBB.....",
    "..LLLLLLLL......",
]
# zampe: colonna di partenza (vicina, lontana) e spostamenti nelle 4 righe sotto il corpo
LEGS = {'front': (8, 9), 'back': (1, 2)}
POSES = {
    'reach': [0, 1, 1, 2],
    'tuck':  [0, 1, 1, None],
    'under': [0, -1, -1, -1],
    'trail': [0, -1, -1, -2],
    'down':  [0, 0, 0, 0],
}
GAIT = [('reach', 'trail'), ('tuck', 'down'), ('under', 'reach'), ('down', 'tuck')]

def reindeer(frame, red=False):
    g = grid(REINDEER + [""] * 4, 16)
    if red:
        g[6][15] = 'N'
    for phase, leg in ((0, 'B'), (1, 'b')):
        front, back = GAIT[(frame + phase * 2) % 4]
        for part, pose in (('front', front), ('back', back)):
            x0 = LEGS[part][phase]
            for row, dx in enumerate(POSES[pose]):
                if dx is None:
                    continue
                if g[13 + row][x0 + dx] == '.':
                    put(g, x0 + dx, 13 + row, leg)
    return g

SLEIGH = [
    "......W...............",
    ".....RRR..............",
    ".....RRRR.............",
    "....WWWWWW............",
    ".....FFEFF............",
    "....WWWWWWF...........",
    ".VV.WWWWWW............",
    "VVVVRWWWWRRR..........",
    "VVVVRKKYKKRRF.........",
    "YYYYYYYYYYYYYYYYY..YY.",
    "RRRRRRRRRRRRRRRRRY.Y.Y",
    ".RRRRRRRRRRRRRRRRRY..Y",
    "..RRRRRRRRRRRRRRRRY.Y.",
    "...rrrrrrrrrrrrrrr.Y..",
    "....Y.....Y.....Y..Y..",
    "....Y.....Y.....Y.Y...",
    ".YYYYYYYYYYYYYYYYYY...",
]

def sleigh_frame(frame):
    g = grid([""] * H_SLEIGH, W_SLEIGH)
    def stamp(art, x, y):
        for yy, row in enumerate(art):
            for xx, c in enumerate(row):
                if c != '.':
                    put(g, x + xx, y + yy, c)
    stamp(SLEIGH, 0, 2)
    # renne: quella dietro e la prima (naso rosso), sfasate di un passo
    R1, R2, TOP = 25, 45, 2
    stamp(reindeer((frame + 1) % 4), R1, TOP)
    stamp(reindeer(frame, red=True), R2, TOP)
    # tiranti (all'altezza del petto) e sonagli al collo
    for x in list(range(21, R1 + 1)) + list(range(R1 + 11, R2 + 1)):
        if g[TOP + 10][x] == '.':
            put(g, x, TOP + 10, 'q')
    put(g, R1 + 9, TOP + 9, 'Y'); put(g, R2 + 9, TOP + 9, 'Y')
    # redini dalla mano di Babbo Natale alle teste: scendono un po' tra un passo e l'altro
    sag = (0, 1, 1, 0)[frame]
    for x in range(13, R2 + 11):
        y = TOP + 8 if x < 16 else TOP + 7 + (sag if 18 < x < R1 + 8 or R1 + 13 < x < R2 + 8 else 0)
        if g[y][x] == '.':
            put(g, x, y, 'q')
    return outline(g, 'o', skip='q')

SLEIGH_FRAMES = [sleigh_frame(i) for i in range(4)]

# neve: mattonella 32 x 6 ripetuta (ferma: è il terreno). Superficie morbida: due dossi larghi
# e bassi (niente punte), c = luce in cima, L = corpo, M = ombra in basso.
import math
def snow_tile(w=32, h=6):
    def surface(x):
        bump = 1.7 * math.exp(-((x - 14) / 5.2) ** 2) + 0.9 * math.exp(-((x - 27) / 3.4) ** 2) + 0.9 * math.exp(-((x + 5) / 3.4) ** 2)
        return h - 4 - round(bump)            # riga della cima (più piccola = più alta)
    rows = []
    for y in range(h):
        row = ''
        for x in range(w):
            top = surface(x)
            depth = y - top
            if depth < 0:
                row += '.'
            elif depth == 0:
                row += 'c'
            elif y >= h - 1 and (x + 3) % 32 < 22 or y == h - 2 and 4 <= (x + 3) % 32 < 13:
                row += 'M'
            else:
                row += 'L'
        rows.append(row)
    return rows
SNOW = snow_tile()
SLEIGH_COLORS = {'o': '3b2418', 'B': '8a5a32', 'b': '6a4325', 'L': 'd2ad83', 'A': 'c9a36e', 'N': 'e2312b', 'n': '2b1b12',
                 'E': '1e1410', 'R': 'c63a2f', 'r': '8f2620', 'Y': 'e7b93e', 'W': 'f7f4ee', 'F': 'f1c6a2', 'K': '2b2522',
                 'V': '2f7a4e', 'q': '5a3a22'}
SNOW_COLORS = {'c': 'ffffff', 'L': 'eaf2f8', 'M': 'cddbe8'}
SNOW_DARK = {'c': 'e3ecf2', 'L': 'b9cad7', 'M': '93a9ba'}   # stessi colori della neve nella barra laterale (tema Natale)

# ---------------------------------------------------------------- output
import zlib, struct, base64, json

CAT_COLORS = {'K': '222228', 'k': '3a3a44', 'W': 'f5f1e8', 'w': 'cdc6b8', 'P': 'ec9aa8',
              'G': 'a3d65e', 'e': '8a8a96', 'Z': '8d97a3', 'o': '222228'}
CAT_DARK = dict(CAT_COLORS, K='3b3e47', k='50535d', o='77808c')
BOAT_COLORS = {'o': '3d4723', 'M': '4c5831', 'S': '94a87c', 's': '7b8f63', 'T': 'dab87f',
               'D': 'b98f58', 'H': '85975f', 'h': '6c7d4c'}
SEA_COLORS = {'c': 'e2f1f8', 'L': '9fcde6', 'M': '7ab6da', 'D': '5f9fca'}
SEA_DARK = {'c': '8fbfd8', 'L': '4f87ad', 'M': '3d7299', 'D': '305f83'}

def png(pixels, colors):
    """pixels: list of rows of chars; '.' transparent. Indexed PNG with tRNS."""
    keys = ['.'] + sorted(colors)
    index = {k: i for i, k in enumerate(keys)}
    h, w = len(pixels), len(pixels[0])
    raw = b''.join(b'\0' + bytes(index[c] for c in row) for row in pixels)
    def chunk(t, d):
        return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    plte = b''.join(bytes.fromhex('000000' if k == '.' else colors[k]) for k in keys)
    data = (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 3, 0, 0, 0))
            + chunk(b'PLTE', plte) + chunk(b'tRNS', b'\0') + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b''))
    return data

def atlas(rows, fw, fh, cols):
    out = []
    for frames in rows:
        for y in range(fh):
            line = []
            for i in range(cols):
                line += frames[i][y] if i < len(frames) else ['.'] * fw
            out.append(line)
    return out

def main():
    names = list(CAT_SHEETS)
    cat_rows = [[outline(pad(f), 'o', skip='Z') for f in CAT_SHEETS[n]] for n in names]
    fh, fw = len(cat_rows[0][0]), len(cat_rows[0][0][0])
    cols = max(len(r) for r in cat_rows)
    img = atlas(cat_rows, fw, fh, cols)
    light, dark = png(img, CAT_COLORS), png(img, CAT_DARK)
    boat_frames = [pad(f) for f in BOAT_FRAMES]
    bh, bw = len(boat_frames[0]), len(boat_frames[0][0])
    boat = png(atlas([boat_frames], bw, bh, len(boat_frames)), BOAT_COLORS)
    sea_img = [list(r) for r in SEA]
    sea, sea_dark = png(sea_img, SEA_COLORS), png(sea_img, SEA_DARK)
    sleigh_frames = [pad(f) for f in SLEIGH_FRAMES]
    sh, sw = len(sleigh_frames[0]), len(sleigh_frames[0][0])
    sleigh = png(atlas([sleigh_frames], sw, sh, len(sleigh_frames)), SLEIGH_COLORS)
    snow_img = [list(r) for r in SNOW]
    snow, snow_dark = png(snow_img, SNOW_COLORS), png(snow_img, SNOW_DARK)
    for name, data in (('cat.png', light), ('cat-dark.png', dark), ('boat.png', boat), ('sea.png', sea), ('sea-dark.png', sea_dark),
                       ('sleigh.png', sleigh), ('snow.png', snow), ('snow-dark.png', snow_dark)):
        open(os.path.join(OUT, name), 'wb').write(data)
    b64 = lambda d: 'data:image/png;base64,' + base64.b64encode(d).decode()
    meta = {'cat': {'fw': fw, 'fh': fh, 'cols': cols, 'rows': {n: [i, len(CAT_SHEETS[n])] for i, n in enumerate(names)}},
            'boat': {'fw': bw, 'fh': bh, 'n': len(boat_frames)}, 'sleigh': {'fw': sw, 'fh': sh, 'n': len(sleigh_frames)}}
    open(os.path.join(OUT, 'sprites.json'), 'w').write(json.dumps({'meta': meta, 'cat': b64(light), 'catDark': b64(dark), 'boat': b64(boat), 'sea': b64(sea), 'seaDark': b64(sea_dark),
                                                               'sleigh': b64(sleigh), 'snow': b64(snow), 'snowDark': b64(snow_dark)}))
    print(json.dumps(meta), 'bytes', len(light), len(dark), len(boat), len(sea), len(sea_dark))

main()
