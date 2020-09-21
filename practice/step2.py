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
print(apple1_w1)
apple1 = src[340:381, 416:475]
w = 475 - 416
h = 386 - 345
cv2.rectangle(src, (416, 340), (416+w, 340+h), (255, 0, 0), 1)
print(w*h)

# apple_1_gray = cv2.cvtColor(apple1, cv2.COLOR_BGR2GRAY)
apple_1_HSV = cv2.cvtColor(apple1, cv2.COLOR_BGR2HSV)
# apple_1_HSV_gray = cv2.cvtColor(apple_1_HSV, cv2.COLOR_BGR2GRAY)
# rt, apple_1_background = cv2.threshold(
#     apple_1_gray, 120, 255, cv2.THRESH_BINARY)


cv2.imshow("apple_1", apple1)
# canny = cv2.Canny(apple_1_HSV, 100, 255)
# cv2.imshow("cnaay", canny)
# cv2.imshow("hsv", apple_1_HSV)
# cv2.imshow("back", apple_1_background)
# cv2.imshow("gray", apple_1_gray)
# cv2.imshow("gray2", apple_1_HSV_gray)

h = 85
print(h)
lower = np.array([h-10])
upper = np.array([h+10])
mask = cv2.inRange(apple_1_HSV[:, :, 0], lower, upper)
result = cv2.bitwise_and(apple_1_HSV, apple_1_HSV, mask=mask)
result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
canny = cv2.Canny(result, 100, 255)
cv2.imshow("res", result)
bw2, bw = cv2.threshold(result, 30, 255, cv2.THRESH_BINARY)

# 그레이 컬러로 바꿔서 바탕 색을 흰색으로 만듬
gray = cv2.cvtColor(bw, cv2.COLOR_BGR2GRAY)
# print(bw)
print(gray)
cv2.imshow("gray", gray)
cv2.imshow("src", src)

a = np.array(gray)

# print(np.count_nonzero(a, axis=0))
zero = np.count_nonzero(a == 0)
noneZero = np.count_nonzero(a)
# 전체값 / 일부값 X 100
re_1 = (noneZero/(zero+noneZero)) * 100
print("============> 답은 !?")
print(" 0 의 갯수는 ? ", zero)
print(" 0 이 아닌 갯수는 ? ", noneZero)
print("(", noneZero, "/(", zero, "+", noneZero, ")) * 100 = ", re_1)
# print(np.count(a))
# print(np.count_zero(a))


# print(ar_1)
# print(np.shape(ar_1))
# cv2.imshow("cnaay", canny)
# cv2.imshow("bw", bw)


# 그레이로 바꾼걸 hsv 로 바꿔서 색만 추출 하고싶었는데 실패
# gray_hsv = cv2.cvtColor(cv2.cvtColor(
#     gray, cv2.COLOR_GRAY2BGR), cv2.COLOR_BGR2HSV)
# cv2.imshow("gray_hsv", gray_hsv)


# contours, hierarchy = cv2.findContours(
#     canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     # print("W :", w)
#     # print("H :", h)
#     area = cv2.contourArea(cnt)
#     # print(area)
#     if area > 85:
#         print("W :", w)
#         print("H :", h)
#         print(area)
#         cv2.rectangle(result, (x, y), (x+w, y+h), (255, 0, 0), 1)

# cv2.imshow("result", result)
# cv2.imshow("res_2", result_2)
# def click_event(event, x, y, flags, param):
# if event == cv2.EVENT_LBUTTONDOWN:
# color = cv2.cvtColor(apple1, cv2.COLOR_BGR2HSV)
# hsv = color[y, x, :]
# print(hsv)

# result = cv2.cvtColor(cv2.cvtColor(
# result, cv2.COLOR_HSV2BGR), cv2.COLOR_BAYER_BG2GRAY)

# res = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)

# 바탕 색과

# canny = cv2.Canny(result, 100, 255)
# cv2.imshow("cnaay", canny)
#     contours, hierarchy = cv2.findContours(
#         canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     area = cv2.contourArea(cnt)
#     cv2.imshow("area", area)
#     # print(area)
#     print(w*h)
#     wh = w*h
#     # if area > 23:
#     cv2.rectangle(apple1, (x, y), (x+w, y+h), (255, 0, 0), 1)
# cv2.rectangle(src, (x, y), (x+w, y+h), (255, 0, 0), 1)

# cv2.imshow("src", src)


# cv2.namedWindow('apple_1')
# cv2.setMouseCallback('apple_1', click_event)

# =================================== apple 2 =========================================
# apple2 = src[335:380, 519:571]
w = 571 - 515
h = 377 - 339
cv2.rectangle(src, (515, 339), (519+w, 339+h), (255, 0, 0), 1)


# ========================================= gosomi 1 =========================================
# gosomi1 = src[338:376, 610:683]
# x: 610, y:341
# x: 646 , y:376

w = 646 - 610
h = 376 - 341
cv2.rectangle(src, (610, 341), (610+w, 341+h), (255, 0, 0), 1)


# ========================================= gosomi 2 =========================================
# gosomi2 = src[338:375, 688:721]
# x:688 , y:340
# x:721 , y:375
w = 721 - 688
h = 375 - 340
cv2.rectangle(src, (688, 340), (688+w, 340+h), (255, 0, 0), 1)


# cv2.imshow("apple_1", apple1)
# cv2.imshow("apple_2", apple2)
# cv2.imshow("gosomi_1", gosomi1)
# cv2.imshow("gosomi_2", gosomi2)
# cv2.imshow("src", src)

cv2.waitKey(0)
cv2.destroyAllWindows()
