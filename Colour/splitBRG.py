# 拆分一幅BGRU图像中的通道
import cv2 as cv
bgr_image=cv.imread("E:/OpenCV/data/cat.jpg")
cv.imshow("5.1",bgr_image)
b,g,r=cv.split(bgr_image)
cv.imshow("B",b)
cv.imshow("G",g)
cv.imshow("R",r)
cv.waitKey()
cv.destroyAllWindows()