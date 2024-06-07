import cv2 as cv
import numpy as np 

# Read the image
img = cv.imread('photoes/cat.jpg')
cv.imshow('cat', img)

blank = np.zeros(img.shape[:2],dtype='uint8')

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2-130),150,255,-1)

mask = cv.bitwise_and(img,img,mask=circle)
cv.imshow('Masked',mask)
cv.waitKey(0)