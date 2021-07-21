import cv2
import numpy as np      # C#의 리스트, 행렬이 포함되어 있지 않기 때문.

# 이미지 로드 기본틀
## 이미지 흐리게 하기(Blur)
## 선명하게
org = cv2.imread('./0719_20/puppy.jpg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(org, (10, 10))
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1 ,0]])
sharp = cv2.filter2D(org, -1, kernel)

cv2.imshow('Original', org)       # 원본
cv2.imshow('Blur', blur)          # 수정본(Blur)
cv2.imshow('Sharp', sharp)        # 수정본(Sharp)

cv2.waitKey(0)                    # 창에서 키입력 대기
cv2.destroyAllWindows()           # 메모리 해제