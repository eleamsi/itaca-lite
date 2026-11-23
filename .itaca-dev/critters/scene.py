import sys; sys.argv=['gen']
exec(open('gen.py').read().replace('\nmain()\n', '\n'))
W, H, S = 64, 21, 10
for fi in (0, 2):
    scene = [['.'] * W for _ in range(H)]
    for y in range(7):
        for x in range(W):
            scene[H - 7 + y][x] = SEA[y][x % 16]
    f = pad(BOAT_FRAMES[fi]); bh = len(f)
    top = H - bh + 1           # bottom: -1 art px
    for y in range(bh):
        for x in range(len(f[0])):
            if f[y][x] != '.' and 0 <= top + y < H: scene[top + y][10 + x] = f[y][x]
    for y in range(4, 7):      # front strip: last 3 tile rows
        for x in range(W):
            scene[H - 7 + y][x] = SEA[y][x % 16]
    big = [[c for c in row for _ in range(S)] for row in scene for _ in range(S)]
    cols = dict(BOAT_COLORS); cols.update(SEA_COLORS)
    open(f'scene{fi}.png', 'wb').write(png(big, cols))
