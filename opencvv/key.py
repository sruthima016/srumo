from array import array

import cv2
import numpy as np

image=cv2.imread('3.jpeg',1)
new_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("hsvimage",new_image)

lower_blue=np.array([110,50,50])
upper_blue=array([130,252,255])
mask=cv2.inRange(new_image,lower_blue,upper_blue)
cv2.imshow("mask",mask)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()