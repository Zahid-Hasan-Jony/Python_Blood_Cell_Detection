import cv2
import numpy as np

"""
params = dict(dp=1,
              minDist=1,
              circles=None,
              param1=300,
              param2=290,
              minRadius=1,
              maxRadius=100)
"""

#img = np.ones((200,250,3), dtype=np.uint8)
img=cv2.imread('/home/zahid/Zahid/cell3.png')
for i in range(50, 80, 1):
    for j in range(40, 70, 1):
        img[i][j]*=200

cv2.circle(img, (120,120), 20, (100,200,80), -1)
img = cv2.medianBlur(img,5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2.5, 15,
              param1=15,
              param2=40,
              minRadius=10,
              maxRadius=18)

#print (circles)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('circles', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
