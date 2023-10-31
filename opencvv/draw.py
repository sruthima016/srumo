import cv2

def draw_circle(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),100,(255,0,0),-1)

image=cv2.imread("1.jpg",1)

scale_percent = 25
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
image = cv2.resize(image, (width, height))


cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_circle)
while (1):
    cv2.imshow("image",image)
    cv2.waitKey(0)
    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()