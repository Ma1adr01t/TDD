"""Generate replaceable draft pixel-art PNGs. Requires Pillow.

These are deliberately temporary assets. The game does NOT run this script;
it only loads PNG files from assets/. Replace any PNG with hand-drawn art later.
"""
from pathlib import Path
from PIL import Image, ImageDraw
import random

OUT = Path(__file__).parent / 'assets'
OUT.mkdir(exist_ok=True)
random.seed(2406)

def new(w, h):
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)

def r(d, box, color):
    d.rectangle(box, fill=color)

def save(im, name):
    im.save(OUT / name)

# Every tile occupies an independent 32x32 atlas cell, arranged left to right.
tile_colors = {
    'grass': ('#718457', '#81915f', '#567347'),
    'grass2': ('#7a8c5d', '#8d9a69', '#5e7950'),
    'asphalt': ('#555856', '#62635d', '#454b49'),
    'asphalt2': ('#505450', '#686960', '#434b49'),
    'sidewalk': ('#9f9a83', '#b5ac90', '#868573'),
    'gravel': ('#8d876d', '#a39b78', '#656855'),
    'cracked': ('#555856', '#696b62', '#323c3b'),
    'roadline': ('#555856', '#696b62', '#d2b66b'),
}
atlas, d = new(32 * len(tile_colors), 32)
for idx, (name, colors) in enumerate(tile_colors.items()):
    x0 = idx * 32
    r(d, (x0, 0, x0 + 31, 31), colors[0])
    if name in ('grass', 'grass2'):
        for j in range(21):
            x, y = random.randrange(32), random.randrange(32)
            r(d, (x0+x, y, x0+x+random.choice((1, 2)), y+1), colors[1 if j%3 else 2])
        for x, y in ((5, 7), (22, 19), (12, 27)):
            r(d, (x0+x, y, x0+x+2, y+3), colors[2])
            r(d, (x0+x+1, y-2, x0+x+2, y), colors[1])
    else:
        for j in range(27):
            x, y = random.randrange(32), random.randrange(32)
            r(d, (x0+x, y, x0+x+random.choice((0,1,2)), y+random.choice((0,1))), colors[1 if j%2 else 2])
        if name == 'sidewalk':
            d.line((x0+1, 16, x0+31, 16), fill='#7d7b69', width=1)
            d.line((x0+16, 0, x0+16, 16), fill='#c3b89a')
            d.line((x0+8, 16, x0+8, 31), fill='#c3b89a')
        if name == 'cracked':
            d.line((x0+2, 18, x0+10, 13, x0+16, 18, x0+21, 10, x0+28, 8), fill='#303c39', width=2)
            d.line((x0+15, 18, x0+15, 24, x0+20, 29), fill='#353f3d', width=1)
        if name == 'roadline':
            r(d, (x0+14, 3, x0+17, 25), '#d8bc78')
save(atlas, 'terrain.png')

ROOF = {'house':'#985b4c','diner':'#a9524b','gas':'#538a91','hall':'#767f96',
        'store':'#a5784a','farm':'#7c8b62','pharmacy':'#649b84','depot':'#726d67','garage':'#627c85'}

def building(kind):
    im, d = new(64, 64)
    roof = ROOF[kind]
    # Southern-facing walls, rooftop, awning, casements and readable entry.
    r(d, (5, 20, 58, 60), '#30433d')
    r(d, (8, 18, 55, 56), '#d9c39b')
    r(d, (8, 34, 55, 36), '#b39b76')
    r(d, (8, 52, 55, 56), '#776c5b')
    r(d, (5, 13, 58, 35), '#3b4846')
    r(d, (7, 11, 56, 32), roof)
    r(d, (9, 12, 54, 14), '#d8ad79')
    r(d, (9, 30, 54, 33), '#554d45')
    for px in range(14, 54, 7):
        r(d, (px, 16, px+2, 18), '#c18f6b')
    for x in (13, 45):
        r(d, (x-1, 38, x+9, 49), '#584e48')
        r(d, (x, 39, x+7, 47), '#729ba6')
        r(d, (x+3, 39, x+4, 47), '#d7c69b')
        r(d, (x, 48, x+7, 49), '#ede3c4')
    r(d, (27, 38, 38, 56), '#4d5048')
    r(d, (28, 39, 37, 56), '#856549')
    r(d, (35, 47, 36, 48), '#f2d17d')
    r(d, (25, 56, 40, 59), '#aaa087')
    if kind == 'house':
        r(d, (11, 5, 51, 13), '#6e4b45')
        r(d, (15, 2, 47, 7), roof)
        r(d, (19, 0, 43, 3), '#c28d74')
        r(d, (45, 2, 49, 14), '#796958')
        r(d, (43, 0, 51, 3), '#625a50')
    if kind in ('diner','store','pharmacy'):
        strip = '#e5e0b9' if kind!='diner' else '#efdec1'
        r(d, (10, 33, 54, 39), strip)
        for x in range(10, 54, 8):
            r(d, (x, 33, x+3, 39), '#b9574d' if kind=='diner' else roof)
        r(d, (17, 19, 47, 27), '#dfc59b')
        for x in range(20, 46, 5):r(d, (x, 21, x+2, 22), '#584f45')
    if kind == 'gas':
        r(d, (0, 39, 9, 58), '#a84438');r(d, (1, 39, 8, 42), '#f4e5bc')
        r(d, (2, 45, 7, 51), '#384f54');r(d, (3, 56, 7, 60), '#413f3c')
        r(d, (1, 11, 61, 16), '#ece4ce')
    if kind == 'hall':
        r(d, (22, 4, 43, 12), '#d2cbb3');r(d, (27, 0, 38, 5), '#d2cbb3')
        r(d, (25, 5, 40, 10), '#7b8294')
        for x in (12, 47):r(d, (x, 37, x+4, 53), '#f0ead2')
    if kind in ('depot','garage','farm'):
        r(d, (15, 36, 49, 56), '#4b5c5f')
        r(d, (18, 39, 46, 55), '#89908a')
        for y in (44, 49):r(d, (18, y, 46, y+1), '#596264')
    save(im, kind+'.png')

for kind in ROOF: building(kind)

im,d=new(18,30)
r(d,(1,1,16,28),'#212a2d');r(d,(3,1,14,28),'#b27c36')
r(d,(4,3,13,26),'#e6b655');r(d,(4,7,13,14),'#244c59')
r(d,(5,8,12,12),'#8db5bd');r(d,(4,20,13,24),'#9c713a')
for x in (0,15):
    for y in (4,20):r(d,(x,y,x+2,y+6),'#202325')
for x in (4,11):
    r(d,(x,0,x+2,2),'#f7ebaf');r(d,(x,27,x+2,29),'#b64e42')
save(im,'car.png')

im,d=new(16,16);r(d,(1,5,13,12),'#343c3a');r(d,(4,3,14,10),'#242b2b');r(d,(6,6,11,8),'#1a2526');r(d,(3,11,7,12),'#77786e');save(im,'pothole.png')
im,d=new(16,16);r(d,(1,7,8,14),'#424b43');r(d,(4,3,12,12),'#b0a178');r(d,(7,4,14,13),'#5b645c');r(d,(9,6,12,7),'#e6dfc0');save(im,'trash.png')
im,d=new(12,12);r(d,(1,2,10,11),'#65452d');r(d,(2,1,9,9),'#cf9651');r(d,(5,1,6,9),'#ead1a0');r(d,(2,4,9,5),'#e8c58d');save(im,'package.png')
im,d=new(24,24);r(d,(6,7,17,17),'#747f78');r(d,(3,9,20,15),'#b8b9a2');r(d,(8,4,15,18),'#ded9bf');r(d,(4,12,19,19),'#9d9f90');save(im,'smoke.png')

print(f'Generated {len(list(OUT.glob("*.png")))} PNG assets in {OUT}')
