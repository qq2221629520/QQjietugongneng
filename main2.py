# 请输入要实现的功能
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxxx
# 打包命令 pyinstaller xxxxxxxx --onefile --icon=xxxxxxxxxx



import cv2
import numpy as np
from PIL import ImageGrab

# 冻结画面并进行鼠标拖动截图
def freeze_screenshot():
    # 对整个屏幕进行截图并保存到内存中
    image = ImageGrab.grab()
    # 将截图转换成OpenCV格式的图像
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    # 在一个窗口中显示截图
    cv2.imshow('screenshot', img)
    # 设置鼠标回调函数
    cv2.setMouseCallback('screenshot', on_mouse)
    # 等待用户进行鼠标拖动操作
    cv2.waitKey(0)

# 鼠标回调函数
def on_mouse(event, x, y, flags, param):
    global point1, point2
    # 当鼠标左键按下时，记录鼠标按下的位置
    if event == cv2.EVENT_LBUTTONDOWN:
        point1 = (x, y)
    # 当鼠标左键释放时，记录鼠标释放的位置，并根据这两个位置计算出需要截取的区域
    elif event == cv2.EVENT_LBUTTONUP:
        point2 = (x, y)
        left = min(point1[0], point2[0])
        top = min(point1[1], point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] - point2[1])
        # 对该区域进行截图并保存到本地
        img = ImageGrab.grab(bbox=(left, top, left+width, top+height))
        img.save('screenshot.png')
        # 关闭窗口
        cv2.destroyAllWindows()

if __name__ == '__main__':
    freeze_screenshot()
