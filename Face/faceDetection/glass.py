# 戴墨镜特效
import cv2 as cv
import dlib
import numpy as np

# 加载预训练的面部特征点检测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# 覆盖图像
def overlay_img(img,img_over,img_over_x,img_over_y):
    img_w,img_h,_ = img.shape                                   # 背景图像宽、高、通道数
    img_over_h,img_over_w,img_over_c = img_over.shape           # 覆盖图像高、宽、通道数
    if img_over_c == 3:
        img_over = cv.cvtColor(img_over,cv.COLOR_BGR2BGRA)      # 转换成4通道图像
    for w in range(0,img_over_w):                               # 遍历列
        for h in range(0,img_over_h):                           # 遍历行
            if img_over[h,w,3] != 0:                            # 如果不是全透明的像素
                for c in range(0,3):                            # 遍历3个通道
                    x = img_over_x + w                          # 覆盖像素的横坐标
                    y = img_over_y + h                          # 覆盖像素的纵坐标
                    if x >= img_w or y >= img_h:                # 如果坐标超出最大宽高
                        break                                   # 不做操作
                    img[y,x,c] = img_over[h,w,c]                # 覆盖像素
    return img                                                  # 完成覆盖的图像

def place_glasses(img, glass_img, landmarks, scale=1.0):
    # 根据眼睛的位置计算眼镜的位置
    left_eye = landmarks.part(36)  # 左眼的外角点
    right_eye = landmarks.part(45)  # 右眼的外角点

    # 计算眼睛中心的y坐标
    eye_center_y = int((left_eye.y + right_eye.y) / 2)

    # 根据眼睛的位置和眼镜的高度计算眼镜的y坐标
    glass_y = eye_center_y - int(glass_img.shape[0] * scale / 2)

    # 保持眼镜宽度不变，根据比例缩放高度
    glass_w = glass_img.shape[1]
    glass_h = int(glass_img.shape[0] * (glass_w / face_img.shape[1]))

    # 缩放眼镜图像
    glass_img = cv.resize(glass_img, (glass_w, glass_h))

    # 计算眼镜的x坐标，假设眼镜中心与眼睛中心对齐
    glass_x = int((left_eye.x + right_eye.x) / 2 - glass_w / 2)

    # 将眼镜放置在计算出的位置
    overlay_img(img, glass_img, glass_x, glass_y)


# 读取图像和加载级联分类器
face_img = cv.imread("model.png")
glass_img = cv.imread("glass.png", cv.IMREAD_UNCHANGED)
face_cascade = cv.CascadeClassifier("E:\Anaconda\A\envs\pythonProject\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

# 转为灰度图像并检测人脸
grayframe = cv.cvtColor(face_img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(grayframe, 1.15, 5)

for rect in faces:
    # 获取面部区域
    face_region = face_img[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]

    # 使用dlib检测面部特征点
    landmarks = predictor(face_region, face_img)

    # 将眼镜放置在脸部的正确位置
    place_glasses(face_img, glass_img, landmarks, scale=1.0)

# 显示结果
cv.imshow("Face with Glasses", face_img)
cv.waitKey(0)
cv.destroyAllWindows()
