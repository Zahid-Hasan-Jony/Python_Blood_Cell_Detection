
from skimage import filters
from scipy import ndimage
import matplotlib.pyplot as plt
import cv2
from skimage import measure 


img = cv2.imread('/home/zahid/Zahid/cell3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
val = filters.threshold_otsu(gray)
drops = ndimage.binary_fill_holes(gray < val)
labels = measure.label(drops)
print('Number of objects',labels.max())

cv2.imshow('detected objects',img)
print('coverage is %f' %(drops.mean()))
plt.imshow(drops, cmap='gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
