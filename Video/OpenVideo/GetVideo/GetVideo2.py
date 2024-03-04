# 动态显示视频文件的属性值
import cv2 as cv
video=cv.VideoCapture("E:/Data/demo.mp4")
fps=video.get(cv.CAP_PROP_FPS)
frame_Num=1
while(video.isOpened()):
    retval,frame=video.read()
    # 设置“Video”窗口的宽为420，高为300
    cv.namedWindow("Video",0)
    cv.resizeWindow("Video",420,300)
    if retval==True:
        # 当前视频播放到第几帧
        cv.putText(frame,"frame:"+str(frame_Num),(0,100),cv.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)
        # 该帧对应着视频的第几秒
        cv.putText(frame,"second:"+str(round(frame_Num/fps,2))+"s",(0,200),cv.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)
        cv.imshow("Video",frame)
    else:
        break
    key=cv.waitKey(50)
    frame_Num+=1
    if key==27:
        break
video.release()
cv.destroyAllWindows()