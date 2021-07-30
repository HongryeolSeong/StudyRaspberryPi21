# 기본 OpenCV 소스
import cv2

cam = cv2.VideoCapture(0)                # 기본 캠
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # 창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 창 높이

fourcc = cv2.VideoWriter_fourcc(*'XVID') # XVID 비디오 코텍
is_record = False                        # 녹화 상태

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 0)     # 상하대칭

    if ret:
        cv2.imshow('Original Video', frame)    # 카메라 영상 Original Video라는 이름으로 창에 띄움

        key = cv2.waitKey(1)
        if key == ord('q'):         # q를 입력받으면
            break                   # 캠 종료
        elif key == ord('c'):       # c를 입력받으면
            cv2.imwrite('./0719_20_21/capture/captured.jpg', frame)
            print('이미지 캡쳐 완료!')
        elif key == ord('r') and is_record == False: # 최초 r을 입력받으면 레코딩 시작
            is_record = True
            Video = cv2.VideoWriter('./0719_20_21/capture/record.avi', fourcc, 20, (frame.shape[1], frame.shape[0]))
            print('녹화시작')
        elif key == ord('r') and is_record == True:  # 녹화중
            is_record = False
            Video.release()
            print('녹화완료')

        if is_record == True:       # 현재화면 녹화
            Video.write(frame)

cam.release()
cv2.destroyAllWindows()