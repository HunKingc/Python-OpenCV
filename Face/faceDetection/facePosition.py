# 在图像的人脸位置绘制红框
import cv2 as cv

img=cv.imread("model.png")
# 加载识别人脸的级联分类器
faceCascade=cv.CascadeClassifier("E:\Anaconda\A\envs\pythonProject\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
faces=faceCascade.detectMultiScale(img,1.15)            # 识别出所有人脸
for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)       # 在图像中人脸的位置绘制方框
    cv.imshow("img",img)
cv.waitKey()
cv.destroyAllWindows()