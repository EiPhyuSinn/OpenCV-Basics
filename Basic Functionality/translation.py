import cv2 as cv 
import numpy as np

# Read the image
img = cv.imread('photoes/cat.jpg')
if img is None:
    print("Error: Could not read the image.")
else:
    cv.imshow("cat", img)

    # Function to translate the image
    def translate(img, x, y):
        transMatrix = np.float32([[1, 0, x], [0, 1, y]])
        dimensions = (img.shape[1], img.shape[0])
        return cv.warpAffine(img, transMatrix, dimensions)

    # -x > left, x > right, -y > down, y > up
    translated_img = translate(img, -100, -100)
    cv.imshow("translated", translated_img)

    # Function to rotate the image
    def rotate(img, angle, rotPoint=None):
        (height, width) = img.shape[:2]

        if rotPoint is None:
            rotPoint = (width // 2, height // 2)
        rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)
        return cv.warpAffine(img, rotMatrix, dimensions)

    # Rotate the image
    rotated = rotate(img, 45)
    rotated1 = rotate(img, -45)
    cv.imshow('rotate', rotated)
    cv.imshow('rotate1', rotated1)

    # Rotate the already rotated image
    double_rotated = rotate(rotate(img, 45), 45)
    cv.imshow('double', double_rotated)

    # Resizing the image
    resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
    cv.imshow("resized",resized)

    # Flipping 
    flip = cv.flip(img,0)
    # 0 > vertically, 1 > horizontally
    # -1 > both vertically and horizontally 
    cv.imshow('flip',flip)

    
    # Wait for a key press and close all windows
    cv.waitKey(0)
    cv.destroyAllWindows()
