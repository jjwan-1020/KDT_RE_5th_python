import cv2
import os
import sys

img_path = os.path.join(os.path.dirname(__file__), "images", "practice.jpg")

img_default = cv2.imread(img_path, cv2.IMREAD_COLOR)
img_grayscale = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

cv2.imshow("Default Image:", img_default)
cv2.imshow("Grayscale Image", img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
