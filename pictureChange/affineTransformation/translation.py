# 让图像向右下方平移
import cv2 as cv
import numpy as np
img=cv.imread("E:/OpenCV/data/cat.jpg")
rows=len(img)                               # 读取图像的行数
cols=len(img[0])                            # 读取图像的列数
M=np.float32([[1,0,50],                     # 横坐标向右移动50像素
                [0,1,100]])                 # 纵坐标向下移动100像素
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow("img",img)
cv.imshow("dst",dst)
cv.waitKey()
cv.destroyAllWindows()