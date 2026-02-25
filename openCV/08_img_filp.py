import cv2
import os

BASE_DIR = os.path.dirname(__file__)
img_path = os.path.join(BASE_DIR, "images", "dog.jpg")

img = cv2.imread(img_path)

img_filp = cv2.flip(img, 1)  # > 0: y축 반전


cv2.imshow("Flip", img_filp)
cv2.waitKey(0)
cv2.destroyAllWindows()
