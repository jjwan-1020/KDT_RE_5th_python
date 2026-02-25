import cv2
import os

BASE_DIR = os.path.dirname(__file__)
img_path = os.path.join(BASE_DIR, "images", "dog.jpg")

img = cv2.imread(img_path)

h, w = img.shape[:2]

img_small = cv2.resize(img, (w // 2, h // 2))
flip_img = cv2.flip(img_small, 1)
dst = img.copy()

y_s = h - flip_img.shape[0]
y_e = h
x_s = w - flip_img.shape[1]
x_e = w

dst[y_s:y_e, x_s:x_e] = flip_img

cv2.imshow("original", img)
cv2.imshow("result", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
