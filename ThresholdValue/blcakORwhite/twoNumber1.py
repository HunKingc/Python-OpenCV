# 二值化处理白黑渐变图
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg",0)           # 将图像读成灰度图像
t1,dst1=cv.threshold(img,127,255,cv.THRESH_BINARY)  # 二值化处理
cv.imshow('img',img)                                # 显示原图
cv.imshow('dst1',dst1)                              # 二值化处理效果图
cv.waitKey()
cv.destroyAllWindows()