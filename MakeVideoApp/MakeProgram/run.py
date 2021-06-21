# 動画作成
import cv2
# 他ファイル
from .makeimage import MakeImage

def MakeVideo():
    # ファイル指定
    DIR = './media/file/'
    # 一枚あたりの表示秒数
    times = 3
    # 画面サイズ
    IMG_SIZE = [1920, 1080]
    # 画像情報
    img_files = MakeImage(IMG_SIZE, DIR)

    fps = len(img_files) / (len(img_files) * times)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter(DIR + 'makemovie/MakeVideo.mp4', fourcc, fps, IMG_SIZE)

    for img_file in img_files:
        img = cv2.imread(img_file)
        video.write(img)

    video.release()
    print('finish!')

    return True