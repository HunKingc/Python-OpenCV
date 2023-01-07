# 为原始图片中匹配成功的区域绘制红框
import cv2 as cv
img=cv.imread("E:/OpenCV/data/background.jpg")
templ=cv.imread("E:/OpenCV/data/template.jpg")
height,width,c=templ.shape                                      # 获取模板图像的高、宽和通道数
result=cv.matchTemplate(img,templ,cv.TM_SQDIFF_NORMED)          # 按照标准平方差方式匹配
# 获取匹配结果中的最小值、最大值、最小值坐标和最大值坐标
minValue,maxValue,minLoc,maxLoc=cv.minMaxLoc(result)
resultPoint1=minLoc                                             # 将最小值坐标当做最佳匹配区域的左上角坐标
# 计算出最佳匹配区域的右下角点坐标
resultPoint2=(resultPoint1[0]+width,resultPoint1[1]+height)
# 在最佳匹配区域位置绘制红色方框，线宽为2像素
cv.rectangle(img,resultPoint1,resultPoint2,(0,0,255),2)
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()