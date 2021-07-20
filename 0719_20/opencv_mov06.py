import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

# 카메라 기본 틀
# 영상 자막 처리
# 영상 캡쳐, 녹화
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔고딕볼드 불러오기
font = ImageFont.truetype('./0719_20/fonts/NanumGothicBold.ttf', 20)

# 저장 영상 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'Xvid')    # HP63
is_record = False   # 녹화상태

while True:
    ret, frame = cap.read()
    h, w, _ = frame.shape   # Width, Channel은 필요없는 경우
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDateTime = now.strftime('%Y%m%d_%H%M%S')    # 20210720_164725

    if ret != True: break

    frame = Image.fromarray(frame)  # 글자 출력을 위해 변환
    draw = ImageDraw.Draw(frame)
    draw.text(xy=(10, (h - 40)), text='실시간 웹캠 - {0}'.format(currDateTime), font=font, fill=(0, 0, 255))
    frame = np.array(frame)         # 원상태 복귀

    cv2.imshow('RealTime CAM', frame)   # 원본
    key = cv2.waitKey(1)
    if key == ord('q'): break
    elif key == ord('c'):
        cv2.imwrite('./0719_20/capture/img_{}.png'.format(fileDateTime), frame)
        print('이미지 저장 완료')
    elif key == ord('r'):   # 레코드 시작
        is_record = True
        video = cv2.VideoWriter('./0719_20/capture/record_{0}.avi'.format(fileDateTime), fourcc, 20, (w, h))
        print('녹화 시작')
    elif key == ord('t'):   # 레코드 종료
        is_record = False
        video.release()     # 객체 해제
        print('녹화 완료')

    # 녹화중 빨간점 표시
    if is_record:
        video.write(frame)
        cv2.circle(img=frame, center=(620, 15), radius=5, color=(0, 0, 255), thickness=3)

cap.release()
cv2.destroyAllWindows()