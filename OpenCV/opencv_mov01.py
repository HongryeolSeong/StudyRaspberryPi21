import cv2
import numpy as np

# 카메라 기본 틀
cap = cv2.VideoCapture(0)    # 웹캠 열기 -> 번호: 0부터 시작 ++
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800) # 넓이와 높이 설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

# 무한루프 (q를 입력할때 까지)
while True:
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에 저장, ret True/False
    frame = cv2.flip(frame, 0)

    if ret != True: break   # ret이 False이면 루프탈출

    # 캠 사이즈 확인용
    #h, w, c = frame.shape
    #print('Width : {0}, Height: {1}, Channel: {2}'.format(w, h, c))

    cv2.imshow('RealTime CAM', frame)   # 로드한 영상을 창에 띄움

    if cv2.waitKey(1) == ord('q'): break    # q입력시 루프 탈출

cap.release()   # 웹캠 해제
cv2.destroyAllWindows()