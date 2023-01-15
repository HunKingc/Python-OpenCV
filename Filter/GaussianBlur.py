# 对猫图像进行高斯滤波操作
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg")
dst1=cv.GaussianBlur(img,(5,5),0,0)
dst2=cv.GaussianBlur(img,(9,9),0,0)
dst3=cv.GaussianBlur(img,(15,15),0,0)
cv.imshow('img',img)
cv.imshow('dst1',dst1)
cv.imshow('dst2',dst2)
cv.imshow('dst3',dst3)
cv.waitKey()
cv.destroyAllWindows()