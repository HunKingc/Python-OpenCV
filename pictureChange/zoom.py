# dsize参数实现缩放
import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg")
dst1=cv.resize(img,(100,100))   # 按照宽100像素、高100像素的大小进行缩小
dst2=cv.resize(img,(400,400))   # 按照宽400像素、高400像素的大小进行放大
cv.imshow("img",img)
cv.imshow("dst1",dst1)
cv.imshow("dst2",dst2)
cv.waitKey()
cv.destroyAllWindows()
# fx和fy参数实现缩放
img1=cv.imread("E:/OpenCV/data/cat.jpg")
dst3=cv.resize(img1,None,fx=1/3,fy=1/2) # 将宽缩小到原来的1/3、高缩小到原来的1/2
dst4=cv.resize(img1,None,fx=2,fy=2)     # 将宽、高放大2倍
cv.imshow("img1",img1)
cv.imshow("dst3",dst3)
cv.imshow("dst4",dst4)
cv.waitKey()
cv.destroyAllWindows()