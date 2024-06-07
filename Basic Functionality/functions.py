import cv2 as cv 

img = cv.imread('photoes/cat.jpg')
cv.imshow("cat",img)


# Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# Bluring the image (to reduce noise in img)
blur = cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# Edge Cascade 
# Edging the blur image is more visible than original
canny = cv.Canny(blur,125,175)
cv.imshow('canny',canny)

#Dilating the image
dilated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dialated',dilated)

# Eroding 
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('eroding',eroded)

# Resize
resize = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized',resize)

# Cropping
cropped = img[100:300,200:500]
cv.imshow('cropped',cropped)
cv.waitKey(0)
