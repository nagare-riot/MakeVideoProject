from PIL import ImageDraw
from .write import Write

def DrawInfo(size, number, imgcanvas, Fontinfo, DIR):

    drawsize = [float(size[0]), float(size[1])]
    draw = ImageDraw.Draw(imgcanvas)
    drawinfo = [
        # [開始地点（横）, 開始地点（縦）, 終了地点（横）, 終了地点（縦）, ブロックの色, ブロックの枠線の色]
        # タイトル
        [float(100), float(50), drawsize[0] / 2, drawsize[1] / 6, [255, 255, 255], [0, 0, 0]],
        # BOX1
        [float(100), drawsize[1] / 4 - 50, drawsize[0] / 2, drawsize[1] / 4 * 3 - 50, [255, 255, 255], [0, 0, 0]],
        # BOX2
        [drawsize[0] / 8, drawsize[1] / 4 * 3, drawsize[0] / 8 * 7, drawsize[1] - 10, [255, 255, 255], [0, 0, 0]],
    ]
    textinfo = Write(drawinfo, Fontinfo, DIR, number)

    return draw, drawinfo, textinfo

def DrawCanvas(draw, drawinfo, textinfo):

    # ブロック
    draw.rectangle((drawinfo[0], drawinfo[1], drawinfo[2], drawinfo[3]),
                    fill=(drawinfo[4][0], drawinfo[4][1], drawinfo[4][2]),
                    outline=(drawinfo[5][0], drawinfo[5][1], drawinfo[5][2]))
    # テキスト
    draw.text((drawinfo[0] + (drawinfo[2] - drawinfo[0]) / 2,
            drawinfo[1] + (drawinfo[3] - drawinfo[1]) / 2),
            textinfo[0], font=textinfo[1], fill=(0, 0, 0), anchor='mm')
    
    return draw

def Draw(size, number, imgcanvas, Fontinfo, DIR):

    draw, drawinfo, textinfo = DrawInfo(size, number, imgcanvas, Fontinfo, DIR)
    for i in range(len(drawinfo)):
        DrawCanvas(draw, drawinfo[i], textinfo[i])

    return draw
