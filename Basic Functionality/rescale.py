import cv2 as cv

def rescaleFrame(frame,scale = 0.75):
    #works for images, videos and livevideos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #works only with liveVideos
    capture.set(3,width)
    capture.set(4,height)

# Reading an image
img = cv.imread('photoes/cat.jpeg') 
img_resized = rescaleFrame(img)
cv.imshow('cat',img)
cv.imshow('cat_resized',img_resized)
cv.waitKey(0)

# Reading a vid
capture = cv.VideoCapture('videos/cat.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=.2)
    cv.imshow('CatVideo',frame)
    cv.imshow('catResized',frame_resized)
   
    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()

