# 绘制一个等腰梯形边框
import numpy as np
import cv2 as cv
# np.zeros：创建了一个画布
# （300,300,3）：一个300*300，具有3个颜色空间的画布
# np.uint8：opencv中的灰度图像和RGB图像都是以uint8存储的，因此这里的类型也是uint8
canvas=np.zeros((300,300,3),np.uint8)
# 按顺时针给出等腰梯形4个顶点的坐标
# 这4个顶点的坐标构成了一个大于等于“顶点个数*1*2“的数组
# 这个数组的数据类型为np.int32
pts=np.array([[100,50],[200,50],[250,250],[50,250]],np.int32)
# 在画布上根据4个顶点的坐标，绘制一个闭合的、红色的、线条宽度为5的等腰梯形边框
canvas=cv.polylines(canvas,[pts],True,(0,0,255),5)
cv.imshow("Polylines",canvas)
cv.waitKey()
cv.destroyAllWindows()