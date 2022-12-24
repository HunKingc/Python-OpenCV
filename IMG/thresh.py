import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/cat.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# Simple Thresholding
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
# Adaptive Thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow('Adaptive Thresholding',adaptive_thresh)
cv.waitKey(0)