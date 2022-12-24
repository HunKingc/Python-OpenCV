import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/yze.jpg")
canny=cv.Canny(img,25,75)
cv.imshow("yze",canny)
cv.waitKey()
cv.destroyAllWindows()