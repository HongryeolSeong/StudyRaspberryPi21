import cv2
import numpy as np

# 카메라 기본 틀
# 영상 자르기
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()

    h, w, c = frame.shape
    crop = frame[:, :int(w/2)]

    if ret != True: break

    cv2.imshow('RealTime CAM', frame)   # 원본
    cv2.imshow('Cropped CAM', crop)     # 수정본


    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()