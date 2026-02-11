import cv2
import os

img = cv2.imread("images/Practice2.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


inverted = 255 - gray_img
cv2.imshow("original", img)
cv2.imshow("Inverted", inverted)
cv2.waitKey(0)
cv2.destroyAllWindows()
