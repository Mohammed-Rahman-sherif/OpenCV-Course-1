import cv2

lion = cv2.imread('resized_lion1.png')
eagle = cv2.imread('resized_eagle1.png')

out = cv2.add(lion,eagle)
normal = lion + eagle
weighted = cv2.addWeighted(lion,0.6,eagle,0.4,0)

cv2.imshow("weighted",weighted)
cv2.imshow("out", out)
cv2.imshow("normal", normal)
cv2.waitKey(0)
cv2.destroyAllWindows()