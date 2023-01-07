# 查找重复的图像
import cv2 as cv
import os
import sys
PIC_PATH="E:\OpenCV\data"
width,height=100,100
pic_file=os.listdir(PIC_PATH)
same_pic_index=[]
imgs=[]
has_same=set()
count=len(pic_file)
if count==0:
    print("没有图像")
    sys.exit(0)
for file_name in pic_file:
    pic_name=PIC_PATH+file_name
    img=cv.imread(pic_name)
    img=cv.resize(img,(width,height))
    imgs.append(img)