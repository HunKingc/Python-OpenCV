# 利用阈值处理勾勒轮廓
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
t1,dst1=cv.threshold(gray,127,255,cv.THRESH_BINARY)
t2,dst2=cv.threshold(gray,127,255,cv.THRESH_BINARY_INV)
cv.imshow('img',img)
cv.imshow('gray',gray)
cv.imshow('dst1',dst1)
cv.imshow('dst2',dst2)
cv.waitKey()
cv.destroyAllWindows()