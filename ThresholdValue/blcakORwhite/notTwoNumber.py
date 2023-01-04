# 对图像进行反二值化处理
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg",0)
t1,dst1=cv.threshold(img,127,255,cv.THRESH_BINARY)      # 二值化处理
t4,dst4=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)  # 反二值化处理
cv.imshow('dst1',dst1)
cv.imshow('dst4',dst4)
cv.waitKey()
cv.destroyAllWindows()