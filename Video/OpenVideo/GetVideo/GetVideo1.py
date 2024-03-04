# 获取并输出视频文件的指定属性值
import cv2
import cv2 as cv
video=cv.VideoCapture("E:/Data/demo.mp4")
fps=video.get(cv.CAP_PROP_FPS)
frame_Count=video.get(cv2.CAP_PROP_FRAME_COUNT)
frame_Width=int(video.get(cv.CAP_PROP_FRAME_WIDTH))
frame_Height=int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
print("帧速率：",fps)
print("帧数：",frame_Count)
print("帧宽度：",frame_Width)
print("帧高度：",frame_Height)