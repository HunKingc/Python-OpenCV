import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/cat.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# Laplaction
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
# Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)
canny=cv.Canny(gray,150,175)
cv.waitKey(0)