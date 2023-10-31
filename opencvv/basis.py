import cv2
img=cv2.imread('1.jpg',0)
cv2.imshow("image",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()