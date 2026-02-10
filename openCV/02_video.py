import cv2
import os

path = os.path.join(os.path.dirname(__file__), "videos", "video.mp4")
print("영상 경로:", path)

cap = cv2.VideoCapture(path)

if not cap.isOpened():
    exit()

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video Player", frame)

    if cv2.waitKey(33) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
