# 绘制一个矩形边框
import numpy as np
import cv2 as cv
# np.zeros():创建一个画布
# (300,300,3):一个300*300，具有3个颜色空间的画布
# np.uint8：opencv中的灰度图像和RGB图像都是以uint8存储的，因此在这里的类型也是uint8
canvas=np.zeros((300,300,3),np.uint8)
# 在画布上绘制一个左上角坐标为（50,50）、右下角坐标为（200,150）、青色的、线条宽度为20的矩形边框
canvas=cv.rectangle(canvas,(50,50),(200,150),(255,255,0),20)
cv.imshow("Rectangle",canvas)
cv.waitKey()
cv.destroyAllWindows()
# canvas=cv.rectangle(canvas,(50,50),(200,150),(255,255,0),-1) 绘制一个实心矩形