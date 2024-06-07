import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv.imread('photos/cat1.jpeg')  # Make sure the path is correct
cv.imshow('cat', img)

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Create a blank mask
blank = np.zeros(gray.shape[:2], dtype='uint8')

# Draw a circle on the mask
circle = cv.circle(blank, (gray.shape[1] // 2, gray.shape[0] // 2), 100, 255, -1)

# Apply the mask to the grayscale image
masked = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('masked', masked)

# Compute the grayscale histogram for the masked area
gray_hist = cv.calcHist([gray], [0], circle, [256], [0, 256])

# Plot the grayscale histogram
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
plt.plot(gray_hist, color='black')
plt.xlim([0, 256])
plt.show()

# Compute and plot the color histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
