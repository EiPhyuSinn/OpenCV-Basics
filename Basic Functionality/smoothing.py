import cv2 as cv

# Read the image
img = cv.imread('photoes/cat1.jpeg')
cv.imshow('cat', img)

# Averging (more kernal size > more blur)
average = cv.blur(img,(7,7))
cv.imshow('average blur',average)

# Gaussian Blur 
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('gaussian blur',gauss)

# Median Blur 
median = cv.medianBlur(img,3)
cv.imshow('Median blur',median)

# Bilateral 
bilateral = cv.bilateralFilter(img,5,15,250)
cv.imshow('Bilateral Blur',bilateral)

cv.waitKey(0)
