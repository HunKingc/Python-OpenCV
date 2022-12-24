# 绘制“交通灯”
import numpy as np
import cv2 as cv
# np.zeros()：创建了一个画布
# （100,300,3）：一个100*300，具有3个颜色空间的画布
# np.uint8：opencv中的灰度图像和RGB图像都是以uint8存储的，因此这里的类型也是uint8
canvas=np.zeros((100,300,3),np.uint8)
# 在画布上，绘制一个圆心坐标为（50,50）、半径为40、红色的实心圆形
canvas=cv.circle(canvas,(50,50),40,(0,0,255),-1)
# 在画布上，绘制一个圆心坐标为（150,50）、半径为40、黄色的实心圆形
canvas=cv.circle(canvas,(150,50),40,(0,255,255),-1)
# 在画布上，绘制一个圆心坐标为（250,50）、半径为40、绿色的实心圆形
canvas=cv.circle(canvas,(250,50),40,(0,255,0),-1)
cv.imshow("TrafficLights",canvas)
cv.waitKey()
cv.destroyAllWindows()