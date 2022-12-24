import cv2 as cv
img=cv.imread("E:/OpenCV/data/cat.jpg")
dst1=cv.flip(img,0)     # 沿X轴翻转
dst2=cv.flip(img,1)     # 沿Y轴翻转
dst3=cv.flip(img,-1)    # 同时沿X轴、Y轴翻转
cv.imshow("img",img)
cv.imshow("dst1",dst1)
cv.imshow("dst2",dst2)
cv.imshow("dst3",dst3)
cv.waitKey()
cv.destroyAllWindows()