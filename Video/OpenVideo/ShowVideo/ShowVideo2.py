# 将视频文件由彩色视频转换为灰度视频
import cv2 as cv
video=cv.VideoCapture("E:/Data/demo.mp4")
while(video.isOpened()):
    retval,img_Color=video.read()
    # 设置“Video”窗口的宽度为420，高为300
    cv.namedWindow("Gray",0)
    cv.resizeWindow("Gray",420,300)
    if retval==True:
        # 把视频由彩色视频转换为灰度视频
        img_Gray=cv.cvtColor(img_Color,cv.COLOR_BGR2GRAY)
        cv.imshow("Gray",img_Gray)
    else:
        break
    key=cv.waitKey(1)
    if key==27:
        break
video.release()
cv.destroyAllWindows()