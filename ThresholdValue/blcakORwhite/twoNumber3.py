# 观察不同最大值的处理效果
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg",0)           # 将图像读成灰度图像
t1,dst1=cv.threshold(img,127,255,cv.THRESH_BINARY)  # 二值化处理
t3,dst3=cv.threshold(img,127,150,cv.THRESH_BINARY)  # 调低最大值效果
cv.imshow('dst1',dst1)                              # 展示最大值为255时的效果
cv.imshow('dst3',dst3)                              # 展示最大值为150时的效果
cv.waitKey()
cv.destroyAllWindows()