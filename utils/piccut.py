from PIL import Image

img1 = Image.open('../static/立直麻将.png')
img2 = Image.open('../static/红宝牌.png')
x = [[247, 362, 353, 532], [], []]
name = ['m', 'p', 's', 'z']

for i in range(1):
    for j in range(9):
        region = img1.crop((x[i][0] + 112 * j, x[i][1], x[i][2] + 112 * j, x[i][3]))
        region = region.resize((105, 170), Image.ANTIALIAS)
        region.save(str(j+1) + name[i] + '.png')

for i in range(3):
    region = img2.crop((65 + 117 * i, 185, 154 + 117 * i, 328))
    region = region.resize((106, 170), Image.ANTIALIAS)
    region.save('r5' + name[i] + '.png')

