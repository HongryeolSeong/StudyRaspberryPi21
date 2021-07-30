import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

# 영상에 글자 출력
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔고딕볼드 불러오기
font = ImageFont.truetype('./0719_20_21/fonts/NanumGothicBold.ttf', 20)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    h, _, _ = frame.shape   # Width, Channel은 필요없는 경우
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')

    if ret != True: break

    frame = Image.fromarray(frame)  # 글자 출력을 위해 변환
    draw = ImageDraw.Draw(frame)
    draw.text(xy=(10, (h - 40)), text='실시간 웹캠 - {0}'.format(currDateTime), font=font, fill=(0, 0, 255))
    frame = np.array(frame)         # 원상태 복귀

    cv2.imshow('RealTime CAM', frame)   # 원본

    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()