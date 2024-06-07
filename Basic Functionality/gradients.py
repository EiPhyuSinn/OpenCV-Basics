import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv.imread('photos/cat1.jpeg')  # Make sure the path is correct
cv.imshow('cat', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Laplacion
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacion,lab')


# Sobel 
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_and(sobelx,sobely)

cv.imshow('Sobel x',sobelx)
cv.imshow('Sobel y',sobely)
cv.imshow('combined sobel',combined_sobel)

canny = cv.Canny(gray,150,175)
cv.imshow('canny',canny)
cv.waitKey(0)