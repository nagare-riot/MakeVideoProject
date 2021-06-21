# テキストファイルの処理（インプット）
import re

def gettext(path):

    path = path + 'text/mytext.txt'

    with open(path) as f:
        GetText = f.read()
    ReplaceText = '@@@'
    text = re.sub('\n', ReplaceText, GetText)
    pattern = 'start.+?end'
    text = re.findall(pattern, text)

    return text, ReplaceText
