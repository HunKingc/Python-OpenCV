import cv2
import numpy
# 1. Paint the image a certain colour
blank=numpy.zeros((500,500,3),dtype='uint8')
blank[200:300,300:400]=0,0,255
# 2. Draw a Rectangle
cv2.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
# 3. Draw a circle
cv2.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# 4. Draw a line
cv2.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
# 5. Write text
cv2.putText(blank,'Hello,my name is Jason!!!',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv2.imshow('Rectangle',blank)
cv2.waitKey(0)