# 读取并显示视频文件
import cv2 as cv
video=cv.VideoCapture("E:/Data/demo.mp4")   # 打开视频文件
while(video.isOpened()):                    # 视频文件被打开
    retval,image=video.read()               # 读取视频文件
    # 设置"Video"窗口的宽为420，高为300
    cv.namedWindow("Video",0)
    cv.resizeWindow("Video",420,300)
    if retval==True:                        # 读取到视频文件
        cv.imshow("Video",image)            # 在窗口中显示读取到的视频文件
    else:                                   # 没有读取到视频文件
        break
    key=cv.waitKey(1)                       # 等待用户按下键盘按键的时间为1ms
    if key == 27:                           # 如果按下Esc键
        break
video.release()                             # 关闭视频文件
cv.destroyAllWindows()                      # 销毁显示视频文件的窗口