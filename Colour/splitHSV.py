# 拆分一幅HSV图像中的通道
import cv2 as cv
bgr_image=cv.imread("E:/OpenCV/data/cat.jpg")
cv.imshow("5.1",bgr_image)
hsv_image=cv.cvtColor(bgr_image,cv.COLOR_BGR2HSV)
h,s,v=cv.split(hsv_image)
cv.imshow("H",h)
cv.imshow("S",s)
cv.imshow("V",v)
cv.waitKey()
cv.destroyAllWindows()