import cv2
import numpy as np      # C#의 리스트, 행렬이 포함되어 있지 않기 때문.

# 이미지 로드 기본틀
## 이미지 대비
org = cv2.imread('./0719_20/puppy.jpg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
enhanced = cv2.equalizeHist(gray)

cv2.imshow('Original', org)        # 원본
cv2.imshow('Gray', gray)           # 그레이
cv2.imshow('Enhanced', enhanced)   # 수정본

cv2.waitKey(0)                     # 창에서 키입력 대기
cv2.destroyAllWindows()            # 메모리 해제