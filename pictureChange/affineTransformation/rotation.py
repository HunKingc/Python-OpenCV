# 让图像逆时针旋转
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg")
rows=len(img)                               # 图像像素行数
cols=len(img[0])                            # 图像像素列数
center=(rows/2,cols/2)                      # 图像的中心点
M=cv.getRotationMatrix2D(center,30,0.8)     # 以图像为中心，逆时针旋转30°，缩放0.8倍
dst=cv.warpAffine(img,M,(cols,rows))        # 按照M进行仿射
cv.imshow("img",img)
cv.imshow("dst",dst)
cv.waitKey()
cv.destroyAllWindows()