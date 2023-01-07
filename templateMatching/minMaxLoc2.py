# 从2幅图像中选择最佳的匹配结果
import cv2 as cv
image=[]                                                            # 储存原始图像的列表
# 向image列表添加原始图像image_221.jpg
image.append(cv.imread("E:/OpenCV/data/image_221.jpg"))
# 向image列表添加原始图像image_222.jpg
image.append(cv.imread("E:/OpenCV/data/image_222.jpg"))
templ=cv.imread("E:/OpenCV/data/template.jpg")                      # 读取模板图像
index=-1                                                            # 初始化车位编号列表的索引为-1
min=1
for i in range(0,len(image)):                                       # 循环匹配image列表中的原始图像
    # 按照标准平方差方式匹配
    results=cv.matchTemplate(image[i],templ,cv.TM_SQDIFF_NORMED)
    # 获得最佳匹配结果的索引
    if min>any(results[0]):
        index=i
cv.imshow('result',image[index])
cv.waitKey()
cv.destroyAllWindows()