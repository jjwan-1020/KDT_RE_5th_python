import cv2
import os

# 경로
base_dir = os.path.dirname(__file__)
video_path = os.path.join(base_dir, "videos", "video.mp4")
output_dir = os.path.join(base_dir, "output")
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    exit()

# 비디오 정보
fourcc = cv2.VideoWriter_fourcc(*"H264")
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(
    os.path.join(output_dir, "video.mp4"), fourcc, fps, (width, height)
)

if not out.isOpened():
    exit()

# 프레임 처리
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    cv2.imshow("Video", frame)

    key = cv2.waitKey(int(1000 / fps)) & 0xFF
    if key == ord("q"):
        cv2.imwrite(os.path.join(output_dir, "video_capture.png"), frame)
        break

out.release()
cap.release()
cv2.destroyAllWindows()
