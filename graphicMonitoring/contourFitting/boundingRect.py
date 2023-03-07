# 为爆炸图形绘制矩形包围框
import cv2 as cv
img=cv.imread("E:/OpenCV/data/shape2.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)                                         # 转灰度
# 进行二值化阈值处理
t,binary=cv.threshold(gray,127,255,cv.THRESH_BINARY)
# 获取二值化图像中的轮廓及轮廓层次
contours,hierarchy=cv.findContours(binary,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
x,y,w,h=cv.boundingRect(contours[0])                                            # 获取第一个轮廓的最小矩形边框，记录坐标、宽和高
cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)                                   # 绘制红色矩形
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()