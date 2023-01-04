# 使用自适应处理的效果
import cv2 as cv
image=cv.imread("E:/OpenCV/data/cat.jpg")
image_Gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
athdMEAM=cv.adaptiveThreshold(image_Gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,3)
athdGAUS=cv.adaptiveThreshold(image_Gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,5,3)
cv.imshow('MEAN_C',athdMEAM)
cv.imshow('GAUSSIAN_C',athdGAUS)
cv.waitKey()
cv.destroyAllWindows()