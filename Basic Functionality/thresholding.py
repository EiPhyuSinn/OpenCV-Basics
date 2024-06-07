import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv.imread('photos/cat1.jpeg')  # Make sure the path is correct
cv.imshow('cat', img)

# BGR > Gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Thresholding is the binarization of the image where pixels has two values (0,1)
# Simple Threadsholding 
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY) #Pixel value that is greater than 150 is set to 255 and less than 150 will be 0 
cv.imshow('Simple thresholding',thresh)

threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) #Pixel value that is greater than 150 is set to 255 and less than 150 will be 0 
cv.imshow('Simple thresholding Inverse',thresh_inv)

# Adaptive thresholding 
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive thresholding',adaptive_thresh)
cv.waitKey(0)