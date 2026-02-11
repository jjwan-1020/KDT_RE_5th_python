import cv2
import os

BASE_DIR = os.path.dirname(__file__)
img_path = os.path.join(BASE_DIR, "images", "dog.jpg")

img = cv2.imread(img_path)

# 이미지 확대
img_up = cv2.pyrUp(img)

# 이미지 축소
img_down = cv2.pyrDown(img)

cv2.imshow("up", img_up)
cv2.imshow("down", img_down)
cv2.waitKey(0)
cv2.destroyAllWindows()
