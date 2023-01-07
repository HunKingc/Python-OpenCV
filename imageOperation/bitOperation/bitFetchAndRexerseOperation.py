# 对猫图像进行取反运算
import cv2 as cv
cat=cv.imread("E:/OpenCV/data/cat.jpg")
img=cv.bitwise_not(cat)                 # 取反运算
cv.imshow('cat',cat)
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()