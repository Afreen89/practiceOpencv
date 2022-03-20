# Video Lesson 1 : Loading images

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# I want to load a jpg image
img  = cv.imread('watch.jpg',cv.IMREAD_GRAYSCALE)

# I want to see the grayscale image using opencv
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

# I want to see the image using matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([50,100],[80, 100],'c', linewidth=5)
plt.show()

# I want to name the image watch.png
cv.imwrite('watchgray.png',img)
