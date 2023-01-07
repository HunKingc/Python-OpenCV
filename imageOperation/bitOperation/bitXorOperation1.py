# 猫图像与十字掩模做异或运算
import cv2 as cv
import numpy as np
cat=cv.imread("E:/OpenCV/data/cat.jpg")
m=np.zeros(cat.shape,np.uint8)
m[120:180,:,:]=255
m[:,80:180,:]=255
img=cv.bitwise_xor(cat,m)               # 异或运算
cv.imshow('cat',cat)
cv.imshow('m',m)
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()