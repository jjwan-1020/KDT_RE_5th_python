import cv2
import os
import sys

# 이미지 파일 경로를 스크립트 기준으로 안전하게 구성
img_path = os.path.join(os.path.dirname(__file__), "images", "dog.jpg")

# # 이미지 읽기
img = cv2.imread(img_path)
# if img is None:
#     print("이미지를 불러올 수 없습니다. 경로를 확인하세요:", img_path)
#     sys.exit(1)
# # 이미지 창에 띄우기
# cv2.imshow("Image Window", img)
# # 키보드 입력 대기 (0은 무한 대기)
# key = cv2.waitKey(0)
# print("pressed key code:", key)
# # 모든 창 닫기
# cv2.destroyAllWindows()

# # 채널 3 (R, G, B)
# img_default = cv2.imread(img_path, cv2.IMREAD_COLOR)
# # 채널 없음(그레이스케일)
# img_grayscale = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# cv2.imshow("Default Image:", img_default)
# cv2.imshow("Grayscale Image", img_grayscale)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

logo_path = os.path.join(os.path.dirname(__file__), "images", "logo.png")

# 채널 3 (R, G, B)
img_default = cv2.imread(logo_path, cv2.IMREAD_COLOR)

# 채널 4 (Alpha 값 포함 - 배경 투명일 경우)
img_unchanged = cv2.imread(logo_path, cv2.IMREAD_UNCHANGED)

cv2.imshow("Default Image:", img_default)
cv2.imshow("Grayscale Image", img_unchanged)
print("LOGO Shape (Unchanged)", img_unchanged.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
