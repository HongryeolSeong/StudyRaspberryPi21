import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

## 함수 선언영역
## 영상 간의 차이나는 부분 표시이미지, 차이나는 픽셀 객수를 리턴하는 함수
def get_diff_image(frame_a, frame_b, frame_c, threshold):
    # 세 개의 모든 프레임을 회식으로 전환
    frame_a_gray = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    frame_b_gray = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
    frame_c_gray = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)

    # a/b 사이 영상 차이 값, b/c 사이 영상 차이 값 구함
    diff_ab = cv2.absdiff(frame_a_gray, frame_b_gray)   # 차이 없음
    diff_bc = cv2.absdiff(frame_b_gray, frame_c_gray)   # 차이 있을 수도 없을 수도 있음

    # 영상 차이 값이 40이상이면 값을 흰 색으로 변환
    ret, diff_ab_t = cv2.threshold(diff_ab, threshold, 255, cv2.THRESH_BINARY)
    ret, diff_bc_t = cv2.threshold(diff_bc, threshold, 255, cv2.THRESH_BINARY)

    # 두 영상에 공통된 부분은 1로 만듦
    diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)
    # 영상에서 1이 된 부분은 확장(morphology)
    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)    # 최종 영상

    diff_cnt = cv2.countNonZero(diff)

    return diff, diff_cnt

# 카메라 기본 틀
# 움직임 발생시 화면 캡쳐
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔고딕볼드 불러오기
font = ImageFont.truetype('./0719_20/fonts/NanumGothicBold.ttf', 20)

# 저장 영상 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'Xvid')    # HP63
is_record = False   # 녹화상태

threshold = 40      # 영상 차이가 나는 threshold 설정
diff_max = 10       # 영상 차이가 나는 최대 픽셀 수

# 초기프레임으로 사용할 프레임 최초 저장
ret, frame_a = cap.read()
ret, frame_b = cap.read()

while True:
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDateTime = now.strftime('%Y%m%d_%H%M%S')    # 20210720_164725

    # 현재영상 입력
    ret, frame = cap.read()
    h, w, _ = frame.shape   # Width, Channel은 필요없는 경우
    
    if ret != True: break

    # 현재영상과 초기영상 비교 후 움직임 감시
    diff, diff_cnt = get_diff_image(frame_a=frame_a, frame_b=frame_b, frame_c=frame, threshold=threshold)

    # 차이나는 이미지 갯수가 10개 이상이 나면 움직임이 발생했다고 판단
    if diff_cnt > diff_max:
        cv2.imwrite('./0719_20_21/capture/img_{}.png'.format(fileDateTime), frame)
        print('움직임 발생. 이미지 캡쳐 완료!')

    # 움직임 결과 영상 출력
    cv2.imshow('Diff Result', diff)

    frame_a = np.array(frame_b)     # 이전화면 이전
    frame_b = np.array(frame)       # 현재화면 이전

    # 영상 자막 출력
    frame = Image.fromarray(frame)  # 글자 출력을 위해 변환
    draw = ImageDraw.Draw(frame)
    draw.text(xy=(10, (h - 40)), text='실시간 웹캠 - {0}'.format(currDateTime), font=font, fill=(0, 0, 255))
    frame = np.array(frame)         # 원상태 복귀

    # 영상 종료시
    key = cv2.waitKey(1)
    if key == ord('q'): break

    cv2.imshow('RealTime CAM', frame)   # 원본

cap.release()
cv2.destroyAllWindows()