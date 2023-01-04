# 利用掩模遮盖相加结果
import cv2 as cv
import numpy as np
img1=np.zeros((150,150,3),np.uint8)
img1[:,:,0]=255
img2=np.zeros((150,150,3),np.uint8)
img2[:,:,2]=255
img=cv.add(img1,img2)
cv.imshow('no mask',img)
m=np.zeros((150,150,1),np.uint8)        # 创建掩模
m[50:100,50:100,:]=255                  # 掩模中央位置为纯白色
cv.imshow('mask',m)
img=cv.add(img1,img2,mask=m)            # 相加时使用掩模
cv.imshow('use mask',img)
cv.waitKey()
cv.destroyAllWindows()