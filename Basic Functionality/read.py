import cv2 as cv

img = cv.imread('photoes/cat.jpeg') 
cv.imshow('cat',img)
cv.waitKey(0)
cv.destroyAllWindows()

capture = cv.VideoCapture('videos/cat.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('CatVideo',frame)
    key = cv.waitKey(20)
    print(f'Key is {key}')
    if key != -1:
        print(f'Pressed key: {chr(key & 0xFF)}')  # Print the pressed key character (for debugging)
    if key & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()