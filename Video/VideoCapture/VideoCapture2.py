# 将摄像头视频由彩色视频转换为灰度视频
import cv2 as cv
capture=cv.VideoCapture(0,cv.CAP_DSHOW)                 # 打开笔记本内置摄像头
while(capture.isOpened()):                              # 笔记本内置摄像头被打开
    retval,image=capture.read()                         # 从摄像头中实时读取视频
    # 把彩色视频转换为灰度视频
    image_Gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    if retval==True:                                    # 读取到摄像头视频后
        cv.imshow("Video",image)                        # 在窗口中显示彩色视频
        cv.imshow("Video_Gray",image_Gray)              # 在窗口中显示灰度视频
        key=cv.waitKey(1)                               # 等待用户按下键盘按键的时间为1ms
        if key==32:                                     # 如果按下空格
            break
capture.release()                                       # 关闭笔记本内置摄像头
cv.destroyAllWindows()                                  # 销毁显示摄像头视频的窗口