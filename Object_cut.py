import cv2

image = cv2.imread('/home/zahid/Zahid/cell3.png')
edged = cv2.Canny(image, 10, 250)

     

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 6))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)


     
(_,cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0 * peri, True)
    cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
idx=0
for c in cnts:
    	x,y,w,h = cv2.boundingRect(c)
    	if w>2 and h>2:
    		idx+=1
    		new_img=image[y:y+h,x:x+w]
    		cv2.imwrite(str(idx) + '.png', new_img)
cv2.imshow("im",image)
cv2.waitKey(0)
    
