# 猫图像与十字掩模做或运算
import cv2 as cv
import numpy as np
cat=cv.imread("E:/OpenCV/data/cat.jpg")
mask=np.zeros(cat.shape,np.uint8)
mask[120:180,:,:]=255
mask[:,80:180,:]=255
img=cv.bitwise_or(cat,mask)             # 或运算
cv.imshow('cat',cat)
cv.imshow('mask',mask)
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()