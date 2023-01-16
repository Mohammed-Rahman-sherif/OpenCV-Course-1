import cv2

lion = cv2.imread('resized_lion1.png', cv2.IMREAD_COLOR)

temp = lion[200:300,300:400]
lion[0:100,0:100] = temp

cv2.imshow('pic',lion)
cv2.waitKey(0)