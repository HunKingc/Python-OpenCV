# 让图像向右倾斜
import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/cat.jpg")
rows=len(img)                               # 图像像素行数
cols=len(img[0])                            # 图像像素列数
p1=np.zeros((3,2),np.float32)               # 32位浮点型空列表，原图3个点
p1[0]=[0,0]                                 # 左上角点坐标
p1[1]=[cols-1,0]                            # 右上角点坐标
p1[2]=[0,rows-1]                            # 左下角点坐标
p2=np.zeros((3,2),np.float32)               # 32位浮点型空列表，倾斜图3个点
p2[0]=[50,0]                                # 左上角点坐标，向右移动50像素
p2[1]=[cols-1,0]                            # 右上角点坐标，位置不变
p2[2]=[0,rows-1]                            # 左下角点坐标，位置不变
M=cv.getAffineTransform(p1,p2)              # 根据3个点的变化轨迹计算出M矩阵
dst=cv.warpAffine(img,M,(cols,rows))        # 按照M进行仿射
cv.imshow("img",img)
cv.imshow("dst",dst)
cv.waitKey()
cv.destroyAllWindows()