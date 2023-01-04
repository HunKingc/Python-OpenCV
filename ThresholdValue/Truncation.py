# 对图像进行截断处理
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg",0)
t1,dst1=cv.threshold(img,127,255,cv.THRESH_BINARY)  # 二值化处理
t7,dst7=cv.threshold(img,127,255,cv.THRESH_TRUNC)   # 截断处理
cv.imshow('dst1',dst1)
cv.imshow('dst7',dst7)
cv.waitKey()
cv.destroyAllWindows()