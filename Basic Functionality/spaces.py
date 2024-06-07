import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# opencv display/loads BGR image so the plot does not know, it does not show in normal way 
# grayscale cannot change to HSV directly, it has to changed to BGR first. 

# Read the image
img = cv.imread('photoes/cat.jpg')
cv.imshow('cat', img)

plt.imshow(img)
plt.show()

#BGR > RGB 
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

# BGR > GrayScale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray) 

# BGR > HSV(huge saturation value)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# BGR > LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)


cv.waitKey(0)