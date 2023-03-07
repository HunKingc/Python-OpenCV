# 为爆炸图像绘制凸包
import cv2 as cv
img=cv.imread("E:/OpenCV/data/shape2.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2RGB)                                          # 转为灰度图像
ret,binary=cv.threshold(gray,127,255,cv.THRESH_BINARY)                          # 二值化处理
# 检测图像中出现的所有轮廓
contours,hierarchy=cv.findContours(binary,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
hull=cv.convexHull(contours[0])                                                 # 获取轮廓的凸包
cv.polylines(img,[hull],True,(0,0,255),2)                                       # 绘制凸包
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()