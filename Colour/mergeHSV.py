# 合并H通道图像、S通道图像和V通道图像
import cv2 as cv
brg_image=cv.imread("E:/OpenCV/data/cat.jpg")
hsv_image=cv.cvtColor(brg_image,cv.COLOR_BGR2HSV)
h,s,v=cv.split(hsv_image)
hsv=cv.merge([h,s,v])
bgr=cv.cvtColor(hsv,cv.COLOR_GRAY2BGR)
cv.imshow("BGR",bgr)
cv.waitKey()
cv.destroyAllWindows()
