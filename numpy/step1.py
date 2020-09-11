import numpy as np
import cv2

a = [1, 2, 3, 4, 5]
b = np.array(a)
c = np.array([1, 3, 5])

# c = b.tolist() list 로 변경

# numpy 에서의 array 의 개념은 행렬, 백터
# numpy 배열

# 타입 확인
# print(type(a))

# 타입 지정
# b = np.array(a,dtype=np.float32)

print(a)
print(b)
print(c)

print("====== 배열 복제 ======")
# ===== 배열 복제
# 원본과 별개의 배열이 생성됩니다.
aa = np.array([1, 2, 3, 4, 5])
bb = aa
cc = aa.copy()

bb[0] = 99

print(aa)
print(bb)
print(cc)

print("====== 배열 계산 ======")
# 리스트에는 사칙 연산 X
# 행렬에는 사칙 연산이 가능하다.
aaa = [1, 2, 3, 4, 5]
bbb = np.array(aaa)
ccc = np.array([1, 3, 5])

print(aaa*2)
print(bbb*2)
print(ccc+3)

# opencv 에서는 uint8 (0~255 까지 사용 가능)
# Signed / UnSigned
# 언사인드 (양수만 0 ~ 255)
# 사인드= 음수 ( -128 ~ 127 )

print("======  다차원 배열 ======")
a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])


print(a1)
print(b1)
print(a1[0][1])
print(b1[0][1][1])
# 배열 보기
# (3,3) 2행 2열 :: 2차원
# (3,2,2) 2행 2열이 3개 있다. :: 3차원
print(">> shape")
print(a1.shape)
print(b1.shape)
# 몇 차원인지
#
print(">> ndim")
print(a1.ndim)
print(a1.ndim)

src = cv2.imread("/Users/triplet_dev/python_study/opencv/image/test.png")
print(src.shape)

# 행렬에 대해서 알자
# 행열에 사칙연산을 알자
# 항등원, 역원


#
