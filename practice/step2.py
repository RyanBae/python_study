import cv2
import numpy as np
# cv2 findContour

# 이미지의 테두리 치기

# (대각선)
# 애플파이 1
# x: 416, y:345
# x: 475, y:381

# 애플파이 2
# x: 519, y:342
# x: 571, y:377

# 고소미 1
# x: 610, y:341
# x: 646 , y:376

# 고소미 2
# x:688 , y:340
# x:721 , y:375


src = cv2.imread(
    "/Users/triplet_dev/python_study/image/snack_01_01_000.png")

height, width = src.shape[:2]
print(height, width)


# ========================================= apple 1 =========================================
apple1_w1 = width-(416)
apple1 = src[340:381, 416:475]
cv2.imshow("apple1", apple1)
w = 475 - 416
h = 386 - 345
cv2.rectangle(src, (416, 340), (416+w, 340+h), (255, 0, 0), 1)
# hsv로 변환
apple_1_HSV = cv2.cvtColor(apple1, cv2.COLOR_BGR2HSV)
# 색상 추출
h = 85
lower = np.array([h-10])
upper = np.array([h+10])
mask = cv2.inRange(apple_1_HSV[:, :, 0], lower, upper)
bw2, bw = cv2.threshold(cv2.cvtColor(cv2.bitwise_and(
    apple_1_HSV, apple_1_HSV, mask=mask), cv2.COLOR_HSV2BGR), 30, 255, cv2.THRESH_BINARY)

# 그레이 컬러로 바꿔서 바탕 색을 흰색으로 만듬
apple_1_gray = cv2.cvtColor(bw, cv2.COLOR_BGR2GRAY)
a = np.array(apple_1_gray)
# print(np.count_nonzero(a, axis=0))
zero = np.count_nonzero(a == 0)
noneZero = np.count_nonzero(a)

cv2.imshow("apple_1_gray", apple_1_gray)
# 전체값 / 일부값 X 100
re_1 = (noneZero/(zero+noneZero)) * 100
# print("============> apple 1 답은 !?")
print(" 0 :: ", zero)
print(" Not 0 :: ", noneZero)
print("apple_1 :: (", noneZero, "/(", zero, "+", noneZero, ")) * 100 = ", re_1)


# =================================== apple 2 =========================================
apple2 = src[335:380, 519:571]
cv2.imshow("apple2", apple2)
w = 571 - 515
h = 377 - 339
cv2.rectangle(src, (515, 339), (519+w, 339+h), (255, 0, 0), 1)

apple_2_HSV = cv2.cvtColor(apple2, cv2.COLOR_BGR2HSV)
# 색상 추출
h = 85
lower = np.array([h-10])
upper = np.array([h+10])
mask = cv2.inRange(apple_2_HSV[:, :, 0], lower, upper)
bw2, bw = cv2.threshold(cv2.cvtColor(cv2.bitwise_and(
    apple_2_HSV, apple_2_HSV, mask=mask), cv2.COLOR_HSV2BGR), 30, 255, cv2.THRESH_BINARY)

# 그레이 컬러로 바꿔서 바탕 색을 흰색으로 만듬
apple_2_gray = cv2.cvtColor(bw, cv2.COLOR_BGR2GRAY)

# numpy 로 0과 0이 아닌 갯수 추출
a = np.array(apple_2_gray)
zero = np.count_nonzero(a == 0)
noneZero = np.count_nonzero(a)

cv2.imshow("apple_2_gray", apple_2_gray)
# 전체값 / 일부값 X 100
re_1 = (noneZero/(zero+noneZero)) * 100
print(" 0 :: ", zero)
print(" Not 0 :: ", noneZero)
print("apple_2 :: (", noneZero, "/(", zero, "+", noneZero, ")) * 100 = ", re_1)


# ========================================= gosomi 1 =========================================
gosomi1 = src[341:376, 610:646]
# gosomi1 = src[338:341, 610:646]
cv2.imshow("gosomi1", gosomi1)
# x: 610, y:341
# x: 646 , y:376

w = 646 - 610
h = 376 - 341
cv2.rectangle(src, (610, 341), (610+w, 341+h), (255, 0, 0), 1)


gosomi_1_HSV = cv2.cvtColor(gosomi1, cv2.COLOR_BGR2HSV)
# 색상 추출
# h = 75
h = 85
lower = np.array([h-10])
upper = np.array([h+10])
mask = cv2.inRange(gosomi_1_HSV[:, :, 0], lower, upper)
bw2, bw = cv2.threshold(cv2.cvtColor(cv2.bitwise_and(
    gosomi_1_HSV, gosomi_1_HSV, mask=mask), cv2.COLOR_HSV2BGR), 30, 255, cv2.THRESH_BINARY)

# 그레이 컬러로 바꿔서 바탕 색을 흰색으로 만듬
gosomi_1_gray = cv2.cvtColor(bw, cv2.COLOR_BGR2GRAY)

# numpy 로 0과 0이 아닌 갯수 추출
a = np.array(gosomi_1_gray)
zero = np.count_nonzero(a == 0)
noneZero = np.count_nonzero(a)


cv2.imshow("bw", bw)
cv2.imshow("gosomi_1_gray", gosomi_1_gray)
# 전체값 / 일부값 X 100
re_1 = (noneZero/(zero+noneZero)) * 100
print(" 0 :: ", zero)
print(" Not 0 :: ", noneZero)
print("gosomi_1 :: (", noneZero, "/(", zero, "+", noneZero, ")) * 100 = ", re_1)


# ========================================= gosomi 2 =========================================
gosomi2 = src[338:375, 688:721]
cv2.imshow("gosomi2", gosomi2)
# x:688 , y:340
# x:721 , y:375
w = 721 - 688
h = 375 - 340
cv2.rectangle(src, (688, 340), (688+w, 340+h), (255, 0, 0), 1)


gosomi_2_HSV = cv2.cvtColor(gosomi2, cv2.COLOR_BGR2HSV)
# 색상 추출
h = 85
lower = np.array([h-10])
upper = np.array([h+10])
mask = cv2.inRange(gosomi_2_HSV[:, :, 0], lower, upper)
bw2, bw = cv2.threshold(cv2.cvtColor(cv2.bitwise_and(
    gosomi_2_HSV, gosomi_2_HSV, mask=mask), cv2.COLOR_HSV2BGR), 30, 255, cv2.THRESH_BINARY)

# 그레이 컬러로 바꿔서 바탕 색을 흰색으로 만듬
gosomi_2_gray = cv2.cvtColor(bw, cv2.COLOR_BGR2GRAY)

# numpy 로 0과 0이 아닌 갯수 추출
a = np.array(gosomi_2_gray)
zero = np.count_nonzero(a == 0)
noneZero = np.count_nonzero(a)

cv2.imshow("gosomi_2_gray", gosomi_2_gray)
# 전체값 / 일부값 X 100
re_1 = (noneZero/(zero+noneZero)) * 100
print(" 0 :: ", zero)
print(" Not 0 :: ", noneZero)
print("gosomi_2 :: (", noneZero, "/(", zero, "+", noneZero, ")) * 100 = ", re_1)


# cv2.imshow("apple_1", apple1)
# cv2.imshow("apple_2", apple2)
# cv2.imshow("gosomi_1", gosomi1)
# cv2.imshow("gosomi_2", gosomi2)
cv2.imshow("src", src)

cv2.waitKey(0)
cv2.destroyAllWindows()
