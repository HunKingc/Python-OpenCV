# 模拟三色光叠加得白光
import cv2 as cv
import numpy as np
img1=np.zeros((150,150,3),np.uint8)         # 创建150*150的0值图像
img1[:,:,0]=255                             # 蓝色通道赋予最大值
img2=np.zeros((150,150,3),np.uint8)
img2[:,:,1]=255                             # 绿色通道赋予最大值
img3=np.zeros((150,150,3),np.uint8)
img3[:,:,2]=255                             # 红色通道赋予最大值
cv.imshow('1',img1)                         # 展示蓝色图像
cv.imshow('2',img2)                         # 展示绿色图像
cv.imshow('3',img3)                         # 展示红色图像
img=cv.add(img1,img2)                       # 蓝色+绿色=青色
cv.imshow('1+2',img)                        # 展示蓝色加绿色的结果
img=cv.add(img,img3)                        # 红色+青色=白色
cv.imshow('1+2+3',img)                      # 展示三色图像相加的结果
cv.waitKey()
cv.destroyAllWindows()