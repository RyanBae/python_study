import numpy as np

# 밥먹듯이 쓰는것
# 슬라이싱, 리쉐이프

print("===== 등간격 =====")
# 백터에 특정 패턴으로 채울때 쓴다.


a = np.arange(0, 10, step=5)
b = np.arange(1, 10, step=5)
c = np.arange(0, 10, step=1)

print(a)
print(b)
print(c)

print("\n")
print("===== 슬라이싱 =====")
#

a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

print("> a1")
print(a1)
print("\n")
print(a1[:, 1:])
print("\n")
print(a1[0:1, 0:2])


print("\n")
print("> a2")
print(a1)
print("\n")
print(a1[::2, ::2])


print("\n")
print("===== 리쉐이프 =====")
# 차원을 줄일때 사용

r = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print("> r")
print(r)
print(np.shape(r))
print('\n')
print("> ReShape >")
r.shape = (6, 2)
print(r)
