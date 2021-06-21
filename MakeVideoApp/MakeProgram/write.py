import re
from PIL import ImageFont
from .gettext import gettext

def Write(drawinfo, Fontinfo, DIR, number):

    textinfo = []
    text = [
        'TITLE\n',
        'BOX①\n',
        'BOX②\n',
    ]
    pattern = [
        'name',
        'text1',
        'text2'
    ]

    string, ReplaceText = gettext(DIR)

    TextMax = []
    for box in drawinfo:
        TxtMax = (box[2] - box[0]) / Fontinfo[1][0]
        if TxtMax % 2 != 0.0:
            TextMax.append(int(TxtMax - TxtMax % 2))
        else:
            TextMax.append(int(TxtMax))

    for i in range(len(drawinfo)):
        # txtファイルからの入力
        txt = re.search(pattern[i] + '.+?' + ReplaceText, string[number]).group()
        txt = txt.replace(pattern[i] + ':', '')
        txt = txt.replace(ReplaceText, '')
        txtbox = re.split('。', txt)
        textbox = []
        for box in txtbox:
            if box != '':
                if i == 2:
                    box += '。'
                    textbox.append(box)
        for box in textbox:
            if len(box) > TextMax[i]:
                for j in range(0, len(box), TextMax[i]):
                    if j != 0:
                        box = box[:j] + '\n' + box[j:]
            if box[:TextMax[i]] == textbox[0][:TextMax[i]]:
                txt = box
            else:
                txt += '\n' + box
        # テキスト情報
        font = ImageFont.truetype(Fontinfo[0], Fontinfo[1][0])
        textinfo.append([text[i] + txt, font])

    return textinfo