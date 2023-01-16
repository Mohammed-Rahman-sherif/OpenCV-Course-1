import cv2
import numpy as np

pic = cv2.imread("desk.jpg", cv2.IMREAD_COLOR)      #cv2.IMREAD_GRAY can be used for gray conversion.
cv2.line(pic,(0,0),(100,100),(255,0,255),10)
#1st - pixels, 2nd - start point, 3rd - end point, 4th - color, 5th - thickness
cv2.imshow("line", pic)



cv2.circle(pic,(250,250),(50),(0,255,255),10)
#1st - pixels, 2nd - center, 3rd - diameter, 4th - color, 5th - thickness
cv2.imshow("circle", pic)



cv2.rectangle(pic,(50,50),(350,150),(255,0,0),10)
#1st - pixels, 2nd - start point, 3rd - end point, 4th - color, 5th - thickness
cv2.imshow("rectangle", pic)



fnt = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(pic,("SHERIF"),(150,300),fnt,1,(255,100,100))
#1st - pixels, 2nd - name, 3rd - where the name to be placed, 4th - font, 5th - thickness, 6th - color
cv2.imshow("NAME", pic)



pnts = np.array([[50,100],[300,150],[546,200],[389,300],[786,350],[554,400]],np.int32)
cv2.polylines(pic,[pnts],True,(255,150,200),5)
#1st - pixels, 2nd - points, 3rd - to connect first and last position, 4th - color, 5th - thickness
cv2.imshow("polylines", pic)
cv2.waitKey(0)
cv2.destroyAllWindows()