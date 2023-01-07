# 猫图像与十字掩模做与运算
import cv2 as cv
import numpy as np
cat=cv.imread("E:/OpenCV/data/cat.jpg")
mask=np.zeros(cat.shape,np.uint8)           # 与猫图像大小相等的掩模图像
mask[120:180,:,:]=255                        # 水平的白色区域
mask[:,80:180,:]=255                        # 垂直的白色区域
img=cv.bitwise_and(cat,mask)                # 与运算
cv.imshow('cat',cat)
cv.imshow('mask',mask)
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()