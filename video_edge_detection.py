import cv2 as cv
video = cv.VideoCapture("C:\\Users\\VIMAL KEERTHI\\Videos\\Captures\\nature.mp4")
while True:
    
    ret,frames = video.read()
    cv.imshow('CAM',frames)
    
    gray = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)
    cv.imshow('GRAY', gray) 
    
    canny_edges = cv.Canny(frames,30,50)
    cv.imshow('CANNY', canny_edges)
    
    k = cv.waitKey(5)
    if k == 27:
        break

video.release()
cv.destroyAllWindows()