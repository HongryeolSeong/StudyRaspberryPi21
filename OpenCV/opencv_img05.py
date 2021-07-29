import cv2
import numpy as np      # C#의 리스트, 행렬이 포함되어 있지 않기 때문.

# 이미지 로드 기본틀
## 노이즈 추가
org = cv2.imread('./0719_20/puppy.jpg', cv2.IMREAD_REDUCED_COLOR_2)
h, w, c = org.shape
noise = np.uint8(np.random.normal(loc=0, scale=80.0, size=[h, w, c]))
noised_img = cv2.add(org, noise)  # 원본이미지에 노이즈 추가

cv2.imshow('Original', org)       # 원본
cv2.imshow('Noise', noised_img)   # 수정본(노이즈)

cv2.waitKey(0)                    # 창에서 키입력 대기
cv2.destroyAllWindows()           # 메모리 해제