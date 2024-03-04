# 读取并显示2个摄像头视频
import cv2 as cv
cap_Inner=cv.VideoCapture(0,cv.CAP_DSHOW)
cap_Outer=cv.VideoCapture(1,cv.CAP_DSHOW)
while(cap_Outer.isOpened() & cap_Inner.isOpened()): # 两个摄像头都打开
    retval,img_Inner=cap_Inner.read()
    ret,img_Outer=cap_Outer.read()
    # 在窗口中显示笔记本内置摄像头读取到的视频
    cv.imshow("Video_Inner",img_Inner)
    # 在窗口中显示连接笔记本外置的摄像头读取到的视频
    cv.imshow("Video_Outer",img_Outer)
    key=cv.waitKey(1)
    if key==32:
        break
cap_Inner.release()
cap_Outer.release()
cv.destroyAllWindows()