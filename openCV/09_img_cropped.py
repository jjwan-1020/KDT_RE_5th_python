import cv2
import os

BASE_DIR = os.path.dirname(__file__)
img_path = os.path.join(BASE_DIR, "images", "dog.jpg")

img = cv2.imread(img_path)

# 이미지 자르기
img_crop = img[100:200, 100:400]

cv2.imshow("original", img)
cv2.imshow("crop", img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
