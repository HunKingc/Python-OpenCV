# 将仙人球图像中的刺抹除
import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/cactus.jpg")
k=np.ones((3,3),np.uint8)                   # 创建3*3的数组作为核
cv.imshow('img',img)
dst=cv.erode(img,k)                         # 腐蚀操作
cv.imshow('dst',dst)
cv.waitKey()
cv.destroyAllWindows()