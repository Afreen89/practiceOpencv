# Video Lesson 1 : Loading images

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img  = cv.imread('watch.jpg',cv.IMREAD_GRAYSCALE)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([50,100],[80, 100],'c', linewidth=5)
plt.show()
cv.imwrite('watchgray.png',img)






