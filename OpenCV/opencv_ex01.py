# 기본 OpenCV 소스
import cv2

cam = cv2.VideoCapture(0)           # 기본 캠
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # 창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 창 높이

while True:
    ret, frame = cam.read()
    #frame = cv2.flip(frame, 0)     # 상하대칭

    if ret:
        cv2.imshow('Original Video', frame)    # 카메라 영상 CAM이라는 이름으로 창에 띄움

        key = cv2.waitKey(1)
        if key == ord('q'):         # q를 입력받으면
            break                   # 캠 종료

cam.release()
cv2.destroyAllWindows()