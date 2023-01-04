# 实现Otus方法的阈值处理
import cv2 as cv
image=cv.imread("E:/OpenCV/data/cat.jpg")
image_Gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
t1,dst1=cv.threshold(image_Gray,127,255,cv.THRESH_BINARY)                               # 二值化处理
# 实现Otsu方法的阈值处理
t2,dst2=cv.threshold(image_Gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.putText(dst2,'best threshold:'+str(t2),(0,30),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)   # 在图像上绘制对合适的阈值
cv.imshow('BINARY',dst1)
cv.imshow('OTSU',dst2)
cv.waitKey()
cv.destroyAllWindows()