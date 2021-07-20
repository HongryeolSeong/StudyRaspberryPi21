import cv2
import numpy as np      # C#의 리스트, 행렬이 포함되어 있지 않기 때문.

# 이미지 로드 기본틀
org = cv2.imread('./0719_20/puppy.jpg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

h, w, c = org.shape

cropped = org[:, :int(w/2)]

cv2.imshow('Original', org)          # cv2 새창 열림
cv2.imshow('Cropped', cropped)       # 반으로 자른 이미지

cv2.waitKey(0)                       # 창에서 키입력 대기
cv2.destroyAllWindows()              # 메모리 해제