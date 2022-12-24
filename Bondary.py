import numpy as np
import cv2 as cv
# 边界检查
img=cv.imread("E:/OpenCV/data/cat.jpg")
canny=cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)
cv.waitKey(0)