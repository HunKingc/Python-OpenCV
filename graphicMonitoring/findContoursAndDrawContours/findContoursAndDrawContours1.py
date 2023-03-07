# 绘制集合图像的轮廓
import cv2 as cv
img=cv.imread("E:/OpenCV/data/shape1.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)                                         # 彩色图像转变成单通道灰度图像
t,binary=cv.threshold(gray,127,255,cv.THRESH_BINARY)                            # 灰度图像转为二值图像
# 检测图像中出现的所有轮廓，记录轮廓的每一个点
contours,hierarchy=cv.findContours(binary,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# 绘制所有轮廓，宽度为5，颜色为红色
cv.drawContours(img,contours,-1,(0,0,255),5)
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()