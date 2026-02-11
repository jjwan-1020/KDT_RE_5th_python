import cv2
import os

BASE_DIR = os.path.dirname(__file__)
v_path = os.path.join(BASE_DIR, "videos", "video.mp4")

cap = cv2.VideoCapture(v_path)

if not cap.isOpened():
    exit()

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    h, w = frame.shape[:2]

    resized = cv2.resize(
        frame, (int(w * 1.5), int(h * 1.5)), interpolation=cv2.INTER_LINEAR
    )

    cv2.imshow("original video", frame)
    cv2.imshow("resize video", resized)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
