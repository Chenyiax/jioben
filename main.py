import pyautogui
import ctypes
import time
import imagesize
import random

try:
    dd=ctypes.cdll.LoadLibrary(".\\DD.dll")
except:
    print('找不到文件：dd.dll')
x=[0,0,0]
y=[0,0,0]
height=[0,0,0]
width=[0,0,0]

while True:
    i = 0
    while i < 3:
        try:
            width[i], height[i] = imagesize.get('target{}.png'.format(i + 1))
            location = pyautogui.locateOnScreen(image='target{}.png'.format(i + 1))
        except:
            x[i] = 0
            y[i] = 0
            print('图片{}不存在'.format(i+1))
        try:
            x[i], y[i] = pyautogui.center(location)
            print('图片{}位置为{},{}'.format(i+1, x[i], y[i]))
            x[i] = x[i] + random.randint(int(width[i] * -1 / 2), int(width[i] / 2))
            y[i] = y[i] + random.randint(int(height[i] * -1 / 2), int(height[i] / 2))
            print('图片{}随机后位置为{},{}'.format(i + 1, x[i], y[i]))
        except:
            x[i] = 0
            y[i] = 0
        if x[i] != 0 and y[i] != 0:
            try:
                dd.DD_mov(int(x[i]), int(y[i]))
                dd.DD_btn(1)
                dd.DD_btn(2)
                print('已成功点击')
                time.sleep(1)
            except:
                print('鼠标移动失败，请尝试使用管理员身份运行此程序')
        i = i + 1
    time.sleep(1)




# #判定目标截图在系统上的位置
# location=pyautogui.locateOnScreen(image='target1.png')
# #输出坐标
# print(location)
#
# #利用center()函数获取目标图像在系统中的中心坐标位置
# x,y=pyautogui.center(location)
# print('center()',x,y)
#
# #对识别出的目标图像进行点击
# #参数x,y代表坐标位置，clicks代表点击次数,button可以设置为左键或者右键
# pyautogui.click(x=x,y=y,clicks=1,button='left')