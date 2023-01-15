# 对猫图像进行中值滤波操作
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg")
dst1=cv.medianBlur(img,3)
dst2=cv.medianBlur(img,5)
dst3=cv.medianBlur(img,7)
dst4=cv.medianBlur(img,9)
cv.imshow('img',img)
cv.imshow('dst1',dst1)
cv.imshow('dst2',dst2)
cv.imshow('dst3',dst3)
cv.imshow('dst4',dst4)
cv.waitKey()
cv.destroyAllWindows()