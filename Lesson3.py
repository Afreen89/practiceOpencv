# Video lesson 5 : image arithmatics and logic

import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

# Load image 1 and image 2
img1 = cv.imread('./Practice_Images/Lesson3_Images/3D-Matplotlib.png') 
img2 = cv.imread('./Practice_Images/Lesson3_Images/mainsvmimage.png') 

# I want to add the images directly
add = img1 + img2

# I want to add the images using opencv
add = cv.add(img1, img2)

# I want to add the weighted images where image 1 is 60% and image 2 is 40%
weighted = cv.addWeighted(img1, 0.6, img2, 0.4, 0)
cv.imshow('weighted', weighted)
cv.waitKey(0)
cv.destroyAllWindows()

 