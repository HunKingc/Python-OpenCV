# 保存一段时长为10s的摄像头视频
import cv2 as cv
capture=cv.VideoCapture(0,cv.CAP_DSHOW)                 # 打开笔记本内置摄像头
fourcc=cv.VideoWriter_fourcc('X','V','I','D')           # 确定视频被保存后的编码格式
fps=20                                                  # 帧速率
# 创建VideoWriter类对象
output=cv.VideoWriter("ten_Seconds.avi",fourcc,fps,(640,480))
frame_Num=10*fps                                        # 时长为10s的摄像头视频含有的帧数
# 笔记本内置摄像头被打开且时长为10s的摄像头视频含有的帧数大于0
while(capture.isOpened() and frame_Num > 0):
    retval,frame=capture.read()
    if retval == True:
        output.write(frame)
        cv.imshow("frame",frame)
    key=cv.waitKey(1)
    frame_Num -= 1                                      # 时长为10s的摄像头视频含有的帧数减少一帧
capture.release()
output.release()
cv.destroyAllWindows()