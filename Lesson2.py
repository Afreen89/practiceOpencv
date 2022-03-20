# Video lesson 4 : Image operations 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# I want to read the image in color
img = cv.imread('watch.jpg', cv.IMREAD_COLOR) # N, M, 3

# I want to separate a pixel on the image and name it px 
img[55, 55] = [255, 255, 255]
px = img[55, 55]
print(px)

# I want to color that pixel white
img[100:200, 100:350] = [255, 255, 255]

# I want to make a copy of the image and save it in watch_face
watch_face = img.copy()[25:100, 100:189]

# I want to see that image where a piece of the image is being cut and pasted in the corner of the original image
watch_face[:,:]= [255,0,0]
img[0:75, 0:89] = watch_face
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()