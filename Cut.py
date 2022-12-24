import cv2 as cv
import numpy as np
# 裁剪
img=cv.imread("E:/OpenCV/data/cat.jpg")
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)