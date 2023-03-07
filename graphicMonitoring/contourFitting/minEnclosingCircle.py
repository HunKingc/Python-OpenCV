# 为爆炸图形绘制图形包围框
import cv2 as cv
img=cv.imread("E:/OpenCV/data/shape2.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)                                         # 变灰度
# 进行二值化处理
t,binary=cv.threshold(gray,127,255,cv.THRESH_BINARY)
# 获取二值化图像中的轮廓及轮廓层次
contours,hierarchy=cv.findContours(binary,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
center,radius=cv.minEnclosingCircle(contours[0])                                # 获取最小圆形边框的圆心点和半径
x=int(round(center[0]))                                                         # 圆心点横坐标转为近似整数
y=int(round(center[1]))                                                         # 圆心点纵坐标转为近似整数
cv.circle(img,(x,y),int(radius),(0,0,255),2)                                    # 绘制圆形
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()