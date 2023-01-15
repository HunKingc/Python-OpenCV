# 对汉字图像进行闭运算
import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/lengxue.jpg")
k=np.ones((15,15),np.uint8)                 # 创建15*15的数组作为核
cv.imshow('img',img)
dst=cv.dilate(img,k)                        # 膨胀操作
dst=cv.erode(dst,k)                         # 腐蚀操作
cv.imshow('dst',dst)                        # 显示闭运算结果
cv.waitKey()
cv.destroyAllWindows()