import numpy as np 
import cv2
import imutils
from PIL import ImageGrab
from pynput.keyboard import Key,Controller
keyboard = Controller()
while True:
	main = ImageGrab.grab(bbox = (690,200,840,320))
	main = np.array(main)
	edged = cv2.Canny(main,75,200)
	cv2.line(main,(int(main.shape[1]/6),0),(int(main.shape[1]/6),int(main.shape[0])),(0,255,0),2)	
	cv2.line(main, (0, int((main.shape[0])/2)), (int(main.shape[1]), int((main.shape[0])/2)), (0,255,0), 2) 
	gray = cv2.cvtColor(main,cv2.COLOR_BGR2GRAY)
	gray = np.float32(gray)
	corners = cv2.goodFeaturesToTrack(gray,50,0.1,10)
	corners = np.int0(corners)
	for corner in corners:
		x,y = corner.ravel()
		if(len(corners)>1):
			if(int((main.shape[0]/6)*5)<y<int(main.shape[0])):
				keyboard.release(Key.down)
				keyboard.press(Key.up)
				break
	cv2.imshow("dhino",main)	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()