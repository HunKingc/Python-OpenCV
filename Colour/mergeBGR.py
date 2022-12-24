# 合并B通道图像、G通道图像和R通道图像
import cv2 as cv
bgr_image=cv.imread("E:/OpenCV/data/cat.jpg")
b,g,r=cv.split(bgr_image)
bgr=cv.merge([b,g,r])
cv.imshow("BGR",bgr)
cv.waitKey()
cv.destroyAllWindows()