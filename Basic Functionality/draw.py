import cv2 as cv
import numpy as np 

# 1. Creating a blank image 
blank = np.ones((500,500,3),dtype='uint8')*255
# Creating an all-green image
# green_color = (0, 255, 0)  # RGB color for green
# blank = np.ones((500, 500, 3), dtype='uint8') * green_color
# cv.imshow("blank",blank)
# cv.waitKey(0)

# 2. Drawing color on blank image
blank[0:200,0:200] = 0,255,0
cv.imshow("Green",blank)
cv.waitKey(0)

# 3. Drawing a rectangle
# cv.rectangle(img=blank,pt1=(0,0),pt2=(200,200),color=(0,255,255),thickness=4)
# cv.rectangle(img=blank,pt1=(0,0),pt2=(200,200),color=(0,255,255),thickness=cv.FILLED)
cv.rectangle(img=blank,pt1=(0,0),pt2=(blank.shape[1]//2,blank.shape[0]//2),color=(0,255,255),thickness=-1)
# will fill the entire rectangle 
cv.imshow('Rectangle',blank)
cv.waitKey(0)

# 4. Draw a circle 

# Draw a filled white circle
cv.circle(img=blank, center=(blank.shape[1] // 2, blank.shape[0] // 2), radius=100, color=(255, 255, 255), thickness=-1)

# Draw a filled white line
cv.line(img=blank, pt1=(0, 0), pt2=(blank.shape[1] // 2, blank.shape[0] // 2), color=(255, 255, 255), thickness=3)

# Display the image with the circle and line
cv.imshow("Circle and Line", blank)

#5. WriteText 
cv.putText(blank,"hi eps",(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("text", blank)
cv.waitKey(0)


