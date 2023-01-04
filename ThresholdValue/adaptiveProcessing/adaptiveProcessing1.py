# 使用常用的5种阈值处理类型对色彩不均衡的图像
import cv2 as cv
image=cv.imread("E:/OpenCV/data/cat.jpg")
image_Gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)                 # 将图像转为灰度图像
t1,dst1=cv.threshold(image_Gray,127,255,cv.THRESH_BINARY)       # 二值化处理
t2,dst2=cv.threshold(image_Gray,127,255,cv.THRESH_BINARY_INV)   # 反二值化处理
t3,dst3=cv.threshold(image_Gray,127,255,cv.THRESH_TOZERO)       # 低于阈值零处理
t4,dst4=cv.threshold(image_Gray,127,255,cv.THRESH_TOZERO_INV)   # 超出阈值零处理
t5,dst5=cv.threshold(image_Gray,127,255,cv.THRESH_TRUNC)        # 截断处理
# 分别显示经过5种阈值类型处理后的图像
cv.imshow('BINARY',dst1)
cv.imshow('BINARY_INV',dst2)
cv.imshow('TOZERO',dst3)
cv.imshow('TOZERO_INV',dst4)
cv.imshow('TRUNC',dst5)
cv.waitKey()
cv.destroyAllWindows()