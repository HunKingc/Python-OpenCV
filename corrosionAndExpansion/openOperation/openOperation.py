# 抹除黑种草图像中的针状叶子
import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/nigella.jpg")
k=np.ones((5,5),np.uint8)                   # 创建5*5的数组作为核
cv.imshow('img',img)
dst=cv.erode(img,k)                         # 腐蚀操作
dst=cv.dilate(dst,k)                        # 膨胀操作
cv.imshow('dst',dst)                        # 显示开运算结果
cv.waitKey()
cv.destroyAllWindows()
