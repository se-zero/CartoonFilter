import cv2
import numpy as np

# 1. 이미지 로드
img = cv2.imread('ironman.jpg')
img = cv2.resize(img, (600, 600))

# 2. Mean Shift Filtering (색상 단순화)
img_filtered = cv2.pyrMeanShiftFiltering(img, sp=25, sr=40)  # sp 값을 올리면 색상이 더 단순화됨

# 3. 그레이스케일 변환
gray = cv2.cvtColor(img_filtered, cv2.COLOR_BGR2GRAY)

# 4. 엣지 검출 (Laplacian)
edges = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)
edges = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY)[1]  # 엣지 강조

# 5. 블러 적용하여 색상 부드럽게 (bilateralFilter 추가)
smooth = cv2.bilateralFilter(img_filtered, d=7, sigmaColor=75, sigmaSpace=75)

# 6. 엣지를 검정색으로 변환 (반전)
edges = cv2.bitwise_not(edges)

# 7. 엣지와 부드러운 색상을 합성하여 만화 효과 적용
cartoon = cv2.bitwise_and(smooth, smooth, mask=edges)

# 결과 출력
cv2.imshow("Cartoonized Image", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
