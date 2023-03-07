# 检测笔图像中出现的直线
import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/pen.png")
o=img.copy()                                    # 复制原图
o=cv.medianBlur(o,5)                            # 使用中值滤波进行降噪
gray=cv.cvtColor(o,cv.COLOR_BGR2GRAY)           # 从彩色图像变成单通道灰度图像
binary=cv.Canny(o,50,150)                       # 绘制边缘图像
# 检测直线，精度为1，全角度，阈值为15，线段最短100，最小间隔18
lines=cv.HoughLinesP(binary,1,np.pi/180,15,minLineLength=100,maxLineGap=18)
for line in lines:                              # 遍历所有直线
    x1,y1,x2,y2=line[0]                         # 读取直线两个端点的坐标
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)    # 在原始图像上绘制直线
cv.imshow('canny',binary)                       # 显示二值化图案
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()