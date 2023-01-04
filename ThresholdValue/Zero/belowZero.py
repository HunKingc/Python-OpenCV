# 对图像进行低于阈值零处理
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg",0)
t5,dst5=cv.threshold(img,127,255,cv.THRESH_TOZERO)  # 低于阈值零处理
cv.imshow('img',img)
cv.imshow('dst5',dst5)
cv.waitKey()
cv.destroyAllWindows()