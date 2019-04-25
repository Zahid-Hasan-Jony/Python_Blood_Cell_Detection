
import cv2
import numpy as np


#Load image
img = cv2.imread('/home/zahid/Zahid/Cell.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#detect circle
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1.1,60,
        param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
#Counting circle
    no_of_circles = 0  
#ensure at least some circles were found
if circles is not None:
#convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")
    no_of_circles = len(circles)
# loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
# draw the circle in the image, then draw a rectangle

        cv2.circle(cimg, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(cimg, (x - 5, y - 5), (x + 5, y + 5), (0, 100, 255), -1)

#output image showing and counting.
cv2.imshow('detected circles',cimg)
print ("no of circles",no_of_circles)
cv2.waitKey(0)
cv2.destroyAllWindows()
