import cv2

image = cv2.imread("1.jpg", 1)


scale_percent = 25
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
small_image = cv2.resize(image, (width, height))


cv2.circle(small_image, (50, 50), 10, (0, 0, 255), -1)
cv2.circle(small_image, (50, small_image.shape[0] - 50), 10, (0, 0, 255), -1)
cv2.circle(small_image, (small_image.shape[1] - 50, 50), 10, (0, 0, 255), -1)
cv2.circle(small_image, (small_image.shape[1] - 50, small_image.shape[0] - 50), 10, (0, 0, 255), -1)


font = cv2.FONT_HERSHEY_COMPLEX
text = "Hello, OpenCV!"
text_size, _ = cv2.getTextSize(text, font, 1, 1)
text_x = (small_image.shape[1] - text_size[0]) // 2
text_y = (small_image.shape[0] + text_size[1]) // 2
cv2.rectangle(small_image, (text_x - 10, text_y - text_size[1] - 10), (text_x + text_size[0] + 10, text_y + 10), (0, 255, 0), -1)
cv2.putText(small_image, text, (text_x, text_y), font, 1, (0, 0, 0), 1)


cv2.line(small_image, (0, 0), (small_image.shape[1], small_image.shape[0]), (255, 0, 0), 5)


cv2.imshow("small_image", small_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
