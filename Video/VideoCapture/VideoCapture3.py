# 显示并保存摄像头视频某一时刻的图像
import cv2 as cv
cap=cv.VideoCapture(0,cv.CAP_DSHOW)
while(cap.isOpened()):
    ret,frame=cap.read()                # 从摄像头中实时读取视频
    cv.imshow("Video",frame)            # 在窗口中显示视频
    k=cv.waitKey(1)                     # 等待用户按下键盘按键的时间为1ms
    if k==32:                           # 按下空格键
        cap.release()                   # 关闭内置摄像头
        cv.destroyAllWindows("Video")   # 销毁名为Video的窗口
        # 保存按下空格键时摄像头视频中的图像
        cv.imwrite("E:\Python\pythonProject\OpenCV\Video\VideoCapture\data/copy.png",frame)
        cv.imshow('img',frame)          # 显示按下空格键时摄像头视频中的图像
        cv.waitKey()                    # 按下任何按键后
        break
cv.destroyAllWindows()