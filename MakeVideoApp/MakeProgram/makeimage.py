# 画像作成
import os
import random
# 他ファイル
from .pastecanvas import PasteCanvas

def MakeImage(size, DIR):

    # 使用する画像フォルダ
    imgDIR = DIR + 'images/'
    # 背景に画像を使う時
    imgback = DIR + 'back/back.jpg'
    # 背景を単色にする時
    imgback = (244, 0, 0)
    # 作成した画像フォルダ
    makeimgDIR = DIR + 'makeimages/'

    # size = [1920, 1080]
    translate = [int(float(size[0]) / 2), 50]
    angle = 0
    scale = 1

    FontDIR = DIR + 'font/SmartFontUI.ttf'
    FontSize = [64, 48]
    Fontinfo = [FontDIR, FontSize]

    ImageDIR = []
    for i in range(7):
        imgback = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        imgpaste = PasteCanvas(i, imgDIR + '0' + str(i + 1) + '.png',
                               imgback, size, translate, angle, scale, Fontinfo, DIR)
        imgpaste.save(os.path.join(makeimgDIR, 'makeimage' + str(i + 1) + '.png'))
        ImageDIR.append(makeimgDIR + 'makeimage' + str(i + 1) + '.png')

    return ImageDIR
