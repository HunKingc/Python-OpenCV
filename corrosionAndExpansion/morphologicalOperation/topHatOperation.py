# 通过顶帽运算画出小蜘蛛的腿
import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/spider.jpg")
k=np.ones((5,5),np.uint8)                   # 创建5*5的数组作为核
cv.imshow('img',img)
dst=cv.morphologyEx(img,cv.MORPH_TOPHAT,k)  # 进行顶帽运算
cv.imshow('dst',dst)                        # 显示顶帽运算结果
cv.waitKey()
cv.destroyAllWindows()