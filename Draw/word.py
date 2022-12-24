# 绘制文字“mrsoft”
import numpy as np
import cv2 as cv
# np.zeros：创建了一个画布
# （300,300,3）：一个300*300，具有3个颜色空间的画布
# np.uint8：opencv中的灰度图像和RGB图像都是以uint8存储的，因此这里的类型也是uint8
canvas=np.zeros((300,300,3),np.uint8)
# 在画布上绘制文字“mrsoft”，文字左下角的坐标为（20,70）
# 字体样式为FONT_HERSHEY_TRIPLEX
# 字体大小为2，线条颜色是绿色，线条宽度为5
cv.putText(canvas,"mrsoft",(20,70),cv.FONT_HERSHEY_TRIPLEX,2,(0,255,0),5)
cv.imshow("Text",canvas)
cv.waitKey()
cv.destroyAllWindows()

