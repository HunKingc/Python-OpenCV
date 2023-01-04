# 观察不同阈值的处理效果
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg",0)           # 将图像读成灰度图像
t1,dst1=cv.threshold(img,127,255,cv.THRESH_BINARY)  # 二值化处理
t2,dst2=cv.threshold(img,210,255,cv.THRESH_BINARY)  # 调高阈值处理
cv.imshow('dst1',dst1)                              # 展示阈值为127时的效果
cv.imshow('dst2',dst2)                              # 展示阈值为210的效果
cv.waitKey()
cv.destroyAllWindows()