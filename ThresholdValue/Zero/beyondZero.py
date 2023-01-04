# 对图像进行超出阈值零处理
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg",0)
t6,dst6=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)  # 超出阈值零处理
cv.imshow('img',img)
cv.imshow('dst6',dst6)
cv.waitKey()
cv.destroyAllWindows()