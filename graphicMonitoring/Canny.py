# 使用Canny算法检测花朵边缘
import cv2 as cv
img=cv.imread("E:/OpenCV/data/flower.png")
r1=cv.Canny(img,10,50);                     # 使用不同的阈值进行边缘检测
r2=cv.Canny(img,100,200);
r3=cv.Canny(img,400,600);
cv.imshow('img',img)
cv.imshow('r1',r1)
cv.imshow('r2',r2)
cv.imshow('r3',r3)
cv.waitKey()
cv.destroyAllWindows()