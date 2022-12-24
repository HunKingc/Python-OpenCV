import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/cat.jpg")
# BGR to Grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# BGR to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# HSV to BGR
lab_bgr=cv.cvtColor(lab,cv.COLOR_Lab2BGR)
cv.waitKey(0)