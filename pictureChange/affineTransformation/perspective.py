# 模拟从底部观察图像得到的透视效果
import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/cat.jpg")
rows=len(img)                                   # 图像像素行数
cols=len(img[0])                                # 图像像素列数
p1=np.zeros((4,2),np.float32)                   # 32位浮点型空列表，保存原图4个点
p1[0]=[0,0]                                     # 左上角点坐标
p1[1]=[cols-1,0]                                # 右上角点坐标
p1[2]=[0,rows-1]                                # 左下角点坐标
p1[3]=[cols-1,rows-1]                           # 右下角点坐标
p2=np.zeros((4,2),np.float32)                   # 32位浮点型空列表，保存透视图4个点
p2[0]=[90,0]                                    # 左上角点坐标，向右移动90像素
p2[1]=[cols-90,0]                               # 右上角点坐标，向左移动90像素
p2[2]=[0,rows-1]                                # 左下角点坐标，位置不变
p2[3]=[cols-1,rows-1]                           # 右下角点坐标，位置不变
M=cv.getPerspectiveTransform(p1,p2)             # 根据4个点的变化轨迹计算出M矩阵
dst=cv.warpPerspective(img,M,(cols,rows))       # 按照M进行仿射
cv.imshow("img",img)
cv.imshow("dst",dst)
cv.waitKey()
cv.destroyAllWindows()