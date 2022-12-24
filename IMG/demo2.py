import cv2 as cv
import numpy as np
img=cv.imread("E:/Data/hhj.jpg")
down_width=700
down_height=900
down_points=(down_width,down_height)
canny=cv.Canny(img,125,175)
new_down=cv.resize(canny,down_points,1)
cv.imshow('hhj',new_down)
cv.waitKey(0)