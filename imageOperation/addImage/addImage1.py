# 分别使用“+”和add()方法计算图像和
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg")
sum1=img+img            # 使用“+”运算符相加
sum2=cv.add(img,img)    # 使用add()方法相加
cv.imshow('sum1',sum1)
cv.imshow('sum2',sum2)
cv.waitKey()
cv.destroyAllWindows()