import cv2

lion = cv2.imread('resized_lion1.png', cv2.IMREAD_COLOR)

a = lion[100,200]
print(a)

#CHANGING COLOR
lion[100:200,200:300] = (0,0,0)

cv2.imshow('pic',lion)
cv2.waitKey(0)