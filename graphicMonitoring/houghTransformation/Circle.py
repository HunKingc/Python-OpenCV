# 检测硬币图像中出现的圆环
import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/coin.png")
o=img.copy()                                    # 复制原图
o=cv.medianBlur(o,5)                            # 使用中值滤波进行降噪
gray=cv.cvtColor(o,cv.COLOR_BGR2GRAY)           # 从彩色图像变成单通道灰度图像
# 检测圆环，圆心最小间距为70，Canny最大阈值为100，投票数超过25，最小半径为10，最大半径为50
circles=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,70,param1=100,param2=25,minRadius=50,maxRadius=100)
circles=np.uint(np.around(circles))             # 将数组元素四舍五入成整数
for c in circles[0]:                            # 遍历圆环结果
    x,y,r=c                                     # 圆心横坐标、纵坐标和圆半径
    cv.circle(img,(x,y),r,(0,0,255),3)          # 绘制圆环
    cv.circle(img,(x,y),2,(0,0,255),3)          # 绘制圆心
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()