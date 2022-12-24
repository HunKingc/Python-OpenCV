import numpy
import cv2 as cv
# 以灰度图的形式读取图像
img = cv.imread("E:/OpenCV/data/cat.jpg",0)
cv.imshow("cat",img)
cv.waitKey(0)


