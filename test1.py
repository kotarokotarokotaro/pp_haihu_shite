import PIL
from PIL import ImageGrab
import time
import datetime
import os
import numpy as np
import sys

x_min = 0 #各自調整してください
x_max = 1440 - 215
y_min = 0
y_max = 900 - 45
interval = 1.0 #画面収録の間隔です
percent = 5.0
threshold = 10.0

area = (x_max - x_min)*(y_max - y_min)

dt_now = datetime.datetime.now()

os.chdir(os.path.expanduser('~'))
filepath = './'
for i in range(10):
    filepath = './Desktop/'+str(dt_now.year)+'_'+str(dt_now.month)+'_'+str(dt_now.day)+'_'+str(i)
    if os.path.exists(filepath) == False :
        os.makedirs(filepath)
        break

save_path = os.path.join(os.path.expanduser('~'),filepath)
os.chdir(save_path)
print('キャプチャを開始します。')
time.sleep(5)

im_mat_past = 0
j = 0

try:
    while True:
        im = ImageGrab.grab(bbox=(x_min, y_min, x_max, y_max))
        im_mat = np.array(im.convert('L'))
        diff = np.abs(im_mat - im_mat_past)
        diff_per = (np.count_nonzero(diff > int(percent * 256.0 / 100.0)) / area ) * 100
        print(diff_per)
        if diff_per > threshold :
            im.save('captured_'+str(j)+'.png')
            j = j + 1
            im_mat_past = im_mat
        time.sleep(interval)

except KeyboardInterrupt:
    print('キャプチャを終了します。')
    sys.exit(0)
