# 绘制花朵的轮廓
import cv2 as cv
img=cv.imread("E:/OpenCV/data/flower.jpg")
cv.imshow('img',img)
img=cv.medianBlur(img,5)                                                        # 使用中值滤波去除噪点
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)                                         # 原图从彩图变成单通道灰度图像
t,binary=cv.threshold(gray,127,255,cv.THRESH_BINARY)                            # 灰度图像转化为二值图像
cv.imshow('binary',binary)                                                      # 显示二值化图像
# 获取二值化图像中的轮廓及轮廓层次
contours,hierarchy=cv.findContours(binary,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
cv.drawContours(img,contours,-1,(0,0,255),2)                                    # 在原图中绘制轮廓
cv.imshow('contours',img)                                                       # 显示绘有轮廓的图像
cv.waitKey()
cv.destroyAllWindows()