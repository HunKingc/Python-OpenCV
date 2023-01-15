# 将图像加工成“近视眼”效果
import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/cat.jpg")
k=np.ones((9,9),np.uint8)               # 创建9*9的数组作为核
cv.imshow('img',img)
dst=cv.dilate(img,k)                    # 膨胀操作
cv.imshow('dst',dst)
cv.waitKey()
cv.destroyAllWindows()