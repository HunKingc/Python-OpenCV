import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/cat.jpg")
# Averaging
average=cv.blur(img,(3,3))
# Gaussion Blur
gauss=cv.GaussianBlur(img,(3,3),0)
# Median Blur
median=cv.medianBlur(img,3)
# Bilateral
bilateral=cv.bilateralFilter(img,10,35,25)
cv.waitKey(0)