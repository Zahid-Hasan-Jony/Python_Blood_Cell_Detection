import cv2
import numpy as np

img = cv2.imread('/home/zahid/Zahid/cell3.png')
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(cimg.shape)

circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,2.5,28,
        param1=15,param2=40,minRadius=10,maxRadius=20)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),2)
no_of_circles = 0  
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    no_of_circles = len(circles)
    for (x, y, r) in circles:
        #cv2.circle(img, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(img,(x+r+2,y-r-2),(x-r-2,y+r+2),(0,255,0),2)
        

cv2.imshow('detected circles',img)
print ("no of circles",no_of_circles)
cv2.waitKey(0)
cv2.destroyAllWindows()
