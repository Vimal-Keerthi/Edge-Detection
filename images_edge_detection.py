

import cv2 as cv

image = cv.imread("D:\pinwheel.jpg")

cv.imshow('RGB',image)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

canny_edges = cv.Canny(image,20,60)
cv.imshow('CANNY',canny_edges)

cv.waitKey(0)
cv.destroyAllWindows()

