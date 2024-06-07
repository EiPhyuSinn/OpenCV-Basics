import cv2 as cv
import numpy as np

# Read the image
img = cv.imread('photoes/cat.jpg')
cv.imshow('cat', img)

blank = np.zeros(img.shape,dtype="uint8")

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Apply Canny edge detection
canny = cv.Canny(gray, 125, 175)
cv.imshow('canny edges', canny)

# bluring the image 
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

# Thresholding the image 
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('threshold',thresh)

# Find contours in the image
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours were found in the image')

# Drawing contours on blank image 
cv.drawContours(blank,contours,-1,(0,255,255),1)
cv.imshow('contours drawn',blank)
cv.waitKey(0)
cv.destroyAllWindows()
