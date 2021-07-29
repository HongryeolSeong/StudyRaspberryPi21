import cv2
import numpy as np
from numpy.core.defchararray import center

org = cv2.imread('./0719/puppy.jpg', cv2.IMREAD_GRAYSCALE)        # 이미지 로드
dst = cv2.resize(org, dsize=(640, 480))

# 도형 그리기
# center = [100, 100] # x, y
# color = (0, 0, 255) # red

# cv2.rectangle(dst, (100, 100), (500, 300), (255, 0, 0))
# cv2.circle(dst, tuple(center), 30, color)


cv2.imshow("origin", dst)                   # 이미지 창 띄우기

cv2.waitKey(0)                              # 키 대기
cv2.destroyAllWindows()                     # OpenCV 인스턴스 종료