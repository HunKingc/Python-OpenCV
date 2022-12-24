import numpy as np
import cv2 as cv
# 利用高斯滤波对图片进行模糊处理
img = cv.imread("E:/OpenCV/data/cat.jpg")
cat = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('cat',cat)
cv.waitKey(0)