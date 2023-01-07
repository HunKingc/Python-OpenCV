# 对图像进行加密、解密
import cv2 as cv
import numpy as np
def encode(img,img_key):                                    # 加密、解密方法
    result=img=cv.bitwise_xor(img,img_key)                  # 两图像做异或运算
    return result
cat=cv.imread("E:/OpenCV/data/cat.jpg")
rows,colmns,channel=cat.shape                               # 原图像的行数、列数和通道数
# 创建与猫图像大小相等的随机像素图像，作为秘钥图像
img_key=np.random.randint(0,256,(rows,colmns,3),np.uint8)
cv.imshow('1',cat)                                          # 展示猫图像
cv.imshow('2',img_key)                                      # 展示秘钥图像
result=encode(cat,img_key)                                  # 对猫图像进行加密
cv.imshow('3',result)                                       # 展示加密图像
result=encode(result,img_key)                               # 对猫图像进行解密
cv.imshow('4',result)                                       # 展示解密图像
cv.waitKey()
cv.destroyAllWindows()