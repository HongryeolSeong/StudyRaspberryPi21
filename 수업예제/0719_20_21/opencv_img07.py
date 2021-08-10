import cv2
import numpy as np      # C#의 리스트, 행렬이 포함되어 있지 않기 때문.

# 이미지 로드 기본틀
## 영상 둘레 표시 컨투어(윤곽)
org = cv2.imread('./0719_20/puppy.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray, 127, 255, 0)
cont, hirc = cv2.findContours(bny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(org, cont, -1, (255, 0, 0), 1)
cv2.imshow('Gray', bny)
cv2.imshow('Result', org)

cv2.waitKey(0)                     # 창에서 키입력 대기
cv2.destroyAllWindows()            # 메모리 해제