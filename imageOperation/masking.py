# 创建3通道掩模图像
import cv2 as cv
import numpy as np
# 创建宽150、高150、3通道、像素类型为无符号8位数字的零值图像
mask=np.zeros((150,150,3),np.uint8)
mask[50:100,20:80,:]=255;           # 50~100行、20~80列的像素改为纯白像素
cv.imshow('mask1',mask)             # 展示掩模
mask[:,:,:]=255;                    # 全部改为纯白像素
mask[50:100,20:80,:]=0;             # 展示掩模
cv.imshow('mask2',mask)
cv.waitKey()
cv.destroyAllWindows()