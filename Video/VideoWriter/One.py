# 保存一段摄像头视频
import cv2 as cv
capture=cv.VideoCapture(0,cv.CAP_DSHOW)                 # 打开笔记本内置摄像头
fourcc=cv.VideoWriter_fourcc('X','V','I','D')           # 确定视频被保存后的编码格式
output=cv.VideoWriter("output.avi",fourcc,20,(640,480)) # 创建VideoWriter类对象
while(capture.isOpened()):                              # 笔记本内置摄像头被打开
    retval,frame=capture.read()                         # 从摄像头中实时读取视频
    if retval == True:                                  # 读取到摄像头视频
        output.write(frame)                             # 在VideoWriter类对象中写入读取到的帧
        cv.imshow("frame",frame)                        # 在窗口中显示摄像头视频
    key=cv.waitKey(1)                                   # 等待用户按下键盘按键的时间为1ms
    if key == 27:                                       # 如果按Esc键
        break
capture.release()
output.release()
cv.destroyAllWindows()