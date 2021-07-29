import cv2
import numpy as np

# 카메라 기본 틀
# 흑백 처리
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret != True: break

    cv2.imshow('RealTime CAM', frame)   # 원본
    cv2.imshow('Gray Result', gray)     # 수정본

    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()