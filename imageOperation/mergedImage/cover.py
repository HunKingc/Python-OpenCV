# 将小猫图像覆盖到沙滩图像上
import cv2 as cv
beach_img=cv.imread("E:/OpenCV/data/beach.jpg")
cat_img=cv.imread("E:/OpenCV/data/cat.jpg")
cat=cat_img[75:400,120:260,:]                       # 截取75~400行、120~260列的像素值组成的图像
cat=cv.resize(cat,(70,160))                         # 将截取出的图像缩放成70*160大小
cv.imshow('cat',cat_img)                            # 展示小猫原始图像
cv.imshow('cat2',cat)                               # 展示截取并缩放的小猫图像
cv.imshow('beach',beach_img)                        # 展示沙滩原始图像
rows,colmns,channel=cat.shape                       # 记录截取图像的行数和列数
# 将沙滩中一部分像素改成截取之后的图像
beach_img[100:100+rows,260:260+colmns,:]=cat
cv.imshow('beach2',beach_img)                       # 展示修改之后的图像
cv.waitKey()
cv.destroyAllWindows()