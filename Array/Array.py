import numpy as np
import cv2 as cv
# 创建一维和二维数组
n1=np.array([1,2,3])
n2=np.array([0.1,0.2,0.3])
n3=np.array([[1,2],[3,4]])
print(n1)
print(n2)
print(n3)
# 创建浮点类型数组
print('***'*20)
list=[1,2,3]
n4=np.array(list,dtype=np.float_)
print(n4)
print(n4.dtype)
print(type(n4[0]))
# 创建三维数组
print('***'*20)
nd1=[1,2,3]
nd2=np.array(nd1,ndmin=3)
print(nd2)
print('***'*20)
# 创建2行3列的未初始化数组
n=np.empty([2,3])
print(n)
print('***'*20)
# 创建纯0数组
n01=np.zeros((3,3),np.uint8)
print(n01)
print('***'*20)
# 创建纯1数组
n02=np.ones((3,3),np.uint8)
print(n02)
print('***'*20)
# 创建随机数组
n03=np.random.randint(1,3,10)
print('随机生成10个1~3且不包括3的整数:',n03)        #随机生成10个1~3且不包括3的整数: [1 1 1 1 1 2 1 2 1 1]
n04=np.random.randint(5,10)
print('size数组大小为空随机返回一个整数:',n04)        #size数组大小为空随机返回一个整数: 6
n05=np.random.randint(5,size=(2,5))
print('随机生成5以内二维数组:',n05)
print('***'*20)
# 对数组做加法运算
n06=np.array([1,2])
n07=np.array([3,4])
print(n06+n07)      #[4 6]
print('***'*20)
# 对数组做减法、乘法和除法运算
n08=np.array([1,2])
n09=np.array([3,4])
print(n08-n09)      #[-2 -2]
print(n08*n09)      #[3 8]
print(n08/n09)      #[0.33333333 0.5       ]
print('***'*20)
# 两个数组做幂运算
n10=np.array([1,2])
n11=np.array([3,4])
print(n10**n11)     #[ 1 16]
print('***'*20)
# 比较运算
n12=np.array([1,2])
n13=np.array([3,4])
print(n12>=n13)     #[False False]
print(n12==n13)     #[False False]
print(n12<=n13)     #[ True  True]
print(n12!=n13)     #[ True  True]
print('***'*20)
# 复制数组，比较复制的结果与原数组是否相同
n14=np.array([1,2])
n15=n14.copy()
print(n14==n15)     #[ True  True]
n15[0]=9
print(n14)          #[1 2]
print(n15)          #[9 2]
print(n14==n15)     #[False  True]
print('***'*20)
# 查找一维数组索引为0的元素
n16=np.array([1,2,3])
print(n16[0])       #1
print('***'*20)
# 切片式索引
n17=np.array([1,2,3])
print(n17[0])       #1
print(n17[1])       #2
print(n17[0:2])     #[1 2]
print(n17[1:])      #[2 3]
print(n17[:2])      #[1 2]
print('***'*20)
# 使用不同的切片式索引操作获取数组中的元素
d=np.array([0,1,2,3,4,5,6,7,8,9])
print(d)            #[0 1 2 3 4 5 6 7 8 9]
print(d[:3])        #[0 1 2]
print(d[3:6])       #[3 4 5]
print(d[6:])        #[6 7 8 9]
print(d[::])        #[0 1 2 3 4 5 6 7 8 9]
print(d[:])         #[0 1 2 3 4 5 6 7 8 9]
print(d[::2])       #[0 2 4 6 8]
print(d[1::5])      #[1 6]
print(d[2::6])      #[2 8]
print(d[::-1])      #[9 8 7 6 5 4 3 2 1 0]
print(d[:-3:-1])    #[9 8]
print(d[-3:-5:-1])  #[7 6]
print(d[-5::-1])    #[5 4 3 2 1 0]
print('***'*20)
# 用3种方式获取二维数组中的元素
m=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(m[1])     #[4 5 6 7]
print(m[1,2])   #6
print(m[-1])    #[ 8  9 10 11]
print('***'*20)
# 对二维数组进行切片式索引操作
l=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(l[:2,1:])
print(l[1,:2])
print(l[:2,2])
print(l[:,:1])
#*********************************************
# 创建纯黑图像
width=200   #图像的宽
height=100  #图像的高
#创建指定宽高、单通道、像素值都为0的图像
img=np.zeros((height,width),np.uint8)
cv.imshow('IMG',img)
cv.waitKey()
cv.destroyAllWindows()
#*********************************************
# 创建纯白图像
width1=200  #图像的宽
height1=100 #图像的高
#创建指定宽高、单通道。像素值都为1的图像
img1=np.ones((height1,width1),np.unit8)*255
cv.imshow('IMG1',img1)
cv.waitKey()
cv.destroyAllWindows()
#*********************************************
# 在黑图像内部绘制白色矩形
width2=200
height2=100
img2=np.zeros((height2,width2),np.uint8)
img2[25:75,50:100]=255  #将图像纵坐标为25~75，横坐标为50~100的区域修改为白色
cv.imshow('IMG2',img2)
cv.waitKey()
cv.destroyAllWindows()
#*********************************************
# 创建黑白相间的图像
width3=200
height3=100
img3=np.zeros((height3,width3),np.uint8)
for i in range(0,width3,40):
    img3[:,i:i+20]=255
cv.imshow('IMG3',img3)
cv.waitKey()
cv.destroyAllWindows()
#*********************************************
# 创建彩色图像
width4=200
height4=100
img4=np.zeros((height4,width4),np.uint8)
blue=img4.copy()    #复制图像
blue[:,:,0]=255     #1通道所有像素为255
green=img4.copy()
green[:,:,1]=255    #2通道所有像素为255
red=img4.copy()
red[:,:,2]=255      #3通道所有像素为255
cv.imshow('BLUE',blue)
cv.imshow('GREEN',green)
cv.imshow('RED',red)
cv.waitKey()
cv.destroyAllWindows()
#*********************************************
# 创建随机图像
width5=200
height5=100
img5=np.random.randint(256,size=(height5,width5),dtype=np.uint8)
cv.imshow('IMG5',img5)
cv.waitKey()
cv.destroyAllWindows()
#*********************************************
# 创建3个一维数组，将这3个数组进行水平拼接
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([7,8,9])
result=np.hstack((a,b,c))
print(result)   #[1,2,3,4,5,6,7,8,9]
#*********************************************
# 创建3个一维数组，将这3个数组进行垂直拼接
a1=np.array([1,2,3])
b1=np.array([4,5,6])
c1=np.array([7,8,9])
result1=np.vstack((a1,b1,c1))
print(result1)  #[[1 2 3] [4 5 6] [7 8 9]]
#*********************************************
# 按照水平和垂直2种方式拼接2幅图像
img6=cv.imread("stone.jpg")
img_h=np.hstack((img6,img6))    # 水平拼接2副图像
img_v=np.vstack((img6,img6))    # 垂直拼接2副图像
cv.imshow("img_h",img_h)
cv.imshow("img_v",img_v)
cv.waitKey()
cv.destroyAllWindows()