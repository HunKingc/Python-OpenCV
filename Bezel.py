import cv2 as cv
import numpy as np
# 显示一个blank空白窗口
img=cv.imread("E:/OpenCV/data/cat.jpg")
black=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',black)
cv.waitKey()
cv.destroyAllWindows()
