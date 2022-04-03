import cv2 as cv
import numpy as np

video = cv.VideoCapture(0);

while True:
    
    ret,frames = video.read()
    cv.imshow('CAM',frames)
    
    gray = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)
    cv.imshow('GRAY', gray)

    canny_edges = cv.Canny(frames,30,75)
    cv.imshow('CANNY', canny_edges)
    
    k = cv.waitKey(5)
    if k == 27:
        break
    
video.release()
cv.destroyAllWindows()

