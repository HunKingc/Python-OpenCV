# 对比高斯滤波核双边滤波的处理效果
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg")
dst1=cv.GaussianBlur(img,(15,15),0,0)       # 使用大小为15*15的滤波核进行高斯滤波
# 双边滤波，选取范围直径为15，颜色差为120
dst2=cv.bilateralFilter(img,15,120,100)
cv.imshow('img',img)
cv.imshow('dst1',dst1)
cv.imshow('dst2',dst2)
cv.waitKey()
cv.destroyAllWindows()