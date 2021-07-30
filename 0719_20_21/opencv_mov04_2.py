import cv2
import numpy as np

# 영상 합치기(원본 + 노이즈 수정본)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)

    h, w, c = frame.shape
    noise = np.uint8(np.random.normal(loc=0, scale=50.0, size=[h, w, c]))
    noised = cv2.add(frame, noise)

    if ret != True: break

    total = cv2.hconcat([frame, noised])  # 영상 합치기
    cv2.imshow('Concat', total)           # 합친 영상 출력

    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()