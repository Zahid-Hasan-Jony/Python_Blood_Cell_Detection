import cv2

img1 = cv2.imread('/home/zahid/Zahid/R.jpg') #change your direction

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 110, 150)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

(_,contours, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    #cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 1)

idx=0
for c in contours:
    	x,y,w,h = cv2.boundingRect(c)
    	if (w>18 and h>18) and (w<35 and h<35):
    		idx+=1
    		new_img=img1[y:y+h,x:x+w]
    		cv2.imwrite(str(idx) + '.png', new_img)

cv2.imshow('detected Edge',edged)
cv2.imshow('detecte Edge',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
