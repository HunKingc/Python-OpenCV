# 通过黑帽运算画出小蜘蛛身上的花纹
import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/spider.jpg")
k=np.ones((5,5),np.uint8)                       # 创建5*5的数组作为核
cv.imshow('img',img)
dst=cv.morphologyEx(img,cv.MORPH_BLACKHAT,k)    # 进行黑帽运算
cv.imshow('dst',dst)                            # 显示黑帽运算结果
cv.waitKey()
cv.destroyAllWindows()