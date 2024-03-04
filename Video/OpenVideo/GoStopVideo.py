# 视频的暂停播放和继续播放
import cv2 as cv
video=cv.VideoCapture("E:/Data/demo.mp4")
while(video.isOpened()):
    retval,image=video.read()
    # 设置“Video”窗口的宽为420，高为300
    cv.namedWindow("Video",0)
    cv.resizeWindow("Video",420,300)
    if retval==True:
        cv.imshow("Video",image)
    else:
        break
    key=cv.waitKey(50)
    if key==32:                         # 按下空格
        cv.waitKey(0)
        continue                        # 再按一次空格，继续播放
    if key==27:                         # 如果按Esc键
        break
video.release()
cv.destroyAllWindows()