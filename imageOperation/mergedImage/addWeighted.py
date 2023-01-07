# 利用计算加权和的方式实现多次曝光效果
import cv2 as cv
sun=cv.imread("E:/OpenCV/data/sun.jpg")
beach=cv.imread("E:/OpenCV/data/beach.jpg")
rows,colmns,channel=sun.shape               # 日落图像的行数、列数和通道数
beach=cv.resize(beach,(colmns,rows))        # 沙滩图像缩放成日落图像的大小
img=cv.addWeighted(sun,0.6,beach,0.6,0)     # 计算两副图像的加权和
cv.imshow('sun',sun)
cv.imshow('beach',beach)
cv.imshow('addWeighted',img)
cv.waitKey()
cv.destroyAllWindows()