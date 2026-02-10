import cv2
import os

path = os.path.join(os.path.dirname(__file__), "videos", "video.mp4")
cap = cv2.VideoCapture(path)

fps = cap.get(cv2.CAP_PROP_FPS)
print("fps", fps)
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print("total frames", total_frames)


while cv2.waitKey(int(1500.0 // fps)) < 0:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == total_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("VideoFrame", frame)

cap.release()
cv2.destroyAllWindows()
