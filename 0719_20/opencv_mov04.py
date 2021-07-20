import cv2
import numpy as np

# 카메라 기본 틀
# 영상 블러 처리
# 영상 노이즈 처리
# 영상 합치기
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    blur = cv2.blur(frame, (50, 50))    # 블러 처리

    h, w, c = frame.shape
    noise = np.uint8(np.random.normal(loc=0, scale=50.0, size=[h, w, c]))
    noised = cv2.add(frame, noise)

    if ret != True: break

    total = cv2.hconcat([frame, noised])  # 영상 합치기
    cv2.imshow('Concat', total)           # 합친 영상 출력

    # cv2.imshow('RealTime CAM', frame)   # 원본
    # cv2.imshow('Blurred CAM', blur)     # 수정본
    # cv2.imshow('Noised CAM', noised)    # 수정본


    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()