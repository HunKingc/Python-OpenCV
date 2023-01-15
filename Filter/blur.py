# 对猫图像进行均值滤波操作
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg")
dst1=cv.blur(img,(3,3))
dst2=cv.blur(img,(5,5))
dst3=cv.blur(img,(7,7))
cv.imshow('img',img)
cv.imshow('dst1',dst1)
cv.imshow('dst2',dst2)
cv.imshow('dst3',dst3)
cv.waitKey()
cv.destroyAllWindows()