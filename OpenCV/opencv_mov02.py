import cv2
import numpy as np

# 회색조 처리
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 회색조 화면 생성

    if ret != True: break

    cv2.imshow('RealTime CAM', frame)   # 원본 출력
    cv2.imshow('Gray Result', gray)     # 수정본 출력

    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()