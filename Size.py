import cv2 as cv
import numpy as np
# 调整尺寸
img=cv.imread("E:/OpenCV/data/cat.jpg")
resized=cv.resize(img,(500,500),1)
cv.imshow('Resized',resized)
cv.waitKey(0)