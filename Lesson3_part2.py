import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 

# I want to read the two images
img1 = cv.imread('./Practice_Images/Lesson3_Images/3D-Matplotlib.png') 
img2 = cv.imread('./Practice_Images/Lesson3_Images/mainlogo.png') 

# I want to know the shape of image 2 and define it in the region of image (roi)
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# I want to create a converted version (gray) pf image 2
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# I want to make a mask of img2 using threshold
ret, mask = cv.threshold(img2gray, 220, 255, cv.THRESH_BINARY_INV)
#cv.imshow('mask', mask)

cv.waitKey(0)
cv.destroyAllWindows()
