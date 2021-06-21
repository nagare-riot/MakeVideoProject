# 画像配置
import cv2
from PIL import Image
from .draw import Draw

def PasteCanvas(number, img, imgback, size, translate, angle, scale, Fontinfo, DIR):
    # 背景の画像の有無により分岐
    source_img = Image.open(img)
    if type(imgback) is str:
        imgcanvas = Image.open(imgback)
    else:
        imgcanvas = Image.new('RGB', (size[0], size[1]), imgback)

    # draw&write
    Draw(size, number, imgcanvas, Fontinfo, DIR)

    # imgファイルのスケールを変更
    imgsize = cv2.imread(img)
    MaxSize = [float(size[0]) / 2 - 150, float(size[1]) / 4 * 3 - 100]
    if imgsize.shape[1] > MaxSize[0] and imgsize.shape[1] >= imgsize.shape[0]:
        scale = MaxSize[0] / imgsize.shape[1]
    elif imgsize.shape[0] > MaxSize[1] and imgsize.shape[0] >= imgsize.shape[1]:
        scale = MaxSize[1] / imgsize.shape[0]

    # imginfo = [weight, height, translateX, translateY]
    imginfo = [imgsize.shape[1] * scale, imgsize.shape[0] * scale]
    imginfo.extend([float(size[0]) / 4 * 3 - imginfo[0] / 2,
                    (MaxSize[1] - imginfo[1]) / 2 + 50])
    for i in range(len(imginfo)):
        if imginfo[i] % 2 != 0:
            imginfo[i] += 1
    source_img = source_img.resize((int(imginfo[0]), int(imginfo[1])))

    # imgファイルを回転
    source_img = source_img.rotate(angle, fillcolor=(255, 128, 0, 0), expand=True)

    # imgファイルを移動・貼り付け
    imgcanvas.paste(source_img, (int(imginfo[2]), int(imginfo[3])))

    return imgcanvas

# フォントについて
# https://www.flopdesign.com/freefont/smartfont.html
