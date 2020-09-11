import cv2
import numpy as np
# cv2 findContour

# 이미지의 테두리 치기

src = cv2.imread(
    "/Users/triplet_dev/python_study/image/find-the-right-box-size.jpg")

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 가장 많이 사용
canny = cv2.Canny(src, 100, 255)
cv2.imshow("cnaay", canny)

# 윤곽선을 파란색으로 만들기
# 이미지에서 같은 레벨의 것들을 골라줌
contours, hierarchy = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    area = cv2.contourArea(cnt)
    # print(area)
    print(w*h)
    wh = w*h
    # if area > 23:
    if wh > 1800 and w > 100 and h > 70:
        cv2.rectangle(src, (x, y), (x+w, y+h), (255, 0, 0), 1)
    # cv2.rectangle(src, (x, y), (x+w, y+h), (255, 0, 0), 1)

cv2.imshow("src", src)

cv2.waitKey(0)
cv2.destroyAllWindows()
