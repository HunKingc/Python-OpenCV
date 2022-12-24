import cv2 as cv
# 从BGR色彩空间转换到GRAY色彩空间
image=cv.imread("E:/OpenCV/data/cat.jpg")
cv.imshow("cat",image)
gray_image=cv.cvtColor(image,cv.COLOR_GRAY2BGRA)
cv.imshow("Gray",gray_image)
cv.waitKey()
cv.destroyAllWindows()
# 从BGR色彩空间转换到HSV色彩空间
image1=cv.imread("E:/OpenCV/data/cat.jpg")
cv.imshow("cat1",image1)
hsv_image=cv.cvtColor(image,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv_image)
cv.waitKey()
cv.destroyAllWindows()