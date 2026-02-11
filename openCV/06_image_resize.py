import cv2
import os

# 1. 이미지 읽기 (흑백으로 로드)
BASE_DIR = os.path.dirname(__file__)
img_path = os.path.join(BASE_DIR, "images", "practice2.jpg")

image = cv2.imread(img_path)

# 2. 고정 크기로 조정 (가로 320, 세로 240)
dst_fixed = cv2.resize(image, (320, 240))

# 3. 비율로 조정  (가로 0.5배, 새로 0.5배)
dst_ratio = cv2.resize(image, None, fx=0.5, fy=0.5)
cv2.imshow("Fixed Resize", dst_fixed)
cv2.imshow("Ratio Resize", dst_ratio)
cv2.waitKey(0)
cv2.destroyAllWindows()
