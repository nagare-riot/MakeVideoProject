from django.shortcuts import render
from MakeVideoApp.MakeProgram.run import MakeVideo
import os

def index(request):

    MakeMovieDIR = './media/file/makemovie/'
    filename = 'MakeVideo.mp4'
    RunBool = False
    ResetBool = False
    Bool = [RunBool, ResetBool]

    if request.method == 'POST':
        if 'button' in request.POST:
            Bool[0] = MakeVideo()
        elif 'reset' in request.POST:
            Bool[1] = True

    if Bool[0] == False:
        if Bool[1] == True and filename in os.listdir('./media/file/makemovie/'):
            os.remove(MakeMovieDIR + filename)
            context = {
                'message': '動画は削除されました。ボタンをクリックして、再度動画が作成できます。'
            }
            Bool[0] = False
            Bool[1] = False
        else:
            context = {
                'message': 'ボタンをクリックして、動画を作成！'
            }
    else:
        context = {
            'message': '動画作成完了！'
        }

    print(Bool)
    print(os.listdir('./media/file/makemovie/'))

    return render(request, 'MakeVideoApp/index.html', context)
