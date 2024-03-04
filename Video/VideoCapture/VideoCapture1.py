# 读取并显示摄像头视频
import cv2 as cv
capture=cv.VideoCapture(0)          # 打开笔记本内置摄像头
while(capture.isOpened()):          # 笔记本内置摄像头被打开
    retval,image=capture.read()     # 从摄像头中实时读取视频
    cv.imshow("Video",image)        # 在窗口中显示读取到的视频
    key=cv.waitKey(1)               # 等待用户按下键盘按键的时间为1ms
    if key==32:                     # 如果按下空格
        break
capture.release()                   # 关闭摄像头
cv.destroyAllWindows()              # 销毁显示摄像头的窗口