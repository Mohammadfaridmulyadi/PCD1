import cv2
import numpy as np
img = cv2.imread("UNTAD.jpg",)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("UNTAD.jpg", img)
cv2.imshow("UNTAD2.jpg", gray)

cv2.waitKey(0)
cv2.destroyAllwindows()
