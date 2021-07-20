import cv2
import numpy as np      # C#의 리스트, 행렬이 포함되어 있지 않기 때문.

# 이미지 로드 기본틀
#org = cv2.imread('./0719_20/puppy.jpg', cv2.IMREAD_GRAYSCALE)            # 흑백으로 로드
org = cv2.imread('./0719_20/puppy.jpg', cv2.IMREAD_REDUCED_COLOR_2)   # 흑백으로 로드(절반 사이즈)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

h, w, c = org.shape
print('Width:{0}, Height:{1}, Channel:{2}'.format(w, h, c))
size_small = cv2.resize(gray, dsize=(int(w/2), int(h/2)))

cv2.imshow('Original', org)          # cv2 원본
cv2.imshow('Gray', gray)             # cv2 흑백
cv2.imshow('Resize', size_small)     # 이미지 반으로 줄임

cv2.waitKey(0)                       # 창에서 키입력 대기
cv2.destroyAllWindows()              # 메모리 해제