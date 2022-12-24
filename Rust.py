import cv2 as cv
import numpy as np
# 腐蚀
img=cv.imread("E:/OpenCV/data/cat.jpg")
canny=cv.Canny(img,125,175)
dilated=cv.dilate(canny,(7,7),iterations=3)
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)
cv.waitKey(0)