import numpy as np


# 배열 생성
# 배열 생성시 초기화
# numpy array 를 만들면서 특정 갑으로 초기화 하여 만들기
# 1 차원 : 백터
# 2 차원 이상 : 행렬
# dtype : 디멘션 타입
print("===== 배열 생성 =====")

# shape 를 직접 넣어줘야함
a = np.ones((2, 2), dtype=int)
b = [1, 2, 3, 4, 5]
# 다른 리스트, 혹은 numpy array 의 내용을 행렬, 1 값으로 바꿈
c = np.ones_like(b, dtype=int)

# 행렬은 비어있을수 없으니 랜덤값으로 넣음.
d = np.empty((2, 2), dtype=int)

# 다른 리스트, 혹은 numpy array 의 내용을 행렬, 0 값으로 바꿈
e = np.zeros_like(b, dtype=int)


print(a)
print('')
# [[1 1]
#  [1 1]]

print(b)
print('')
# [1, 2, 3, 4, 5]

print(c)
print('')
# [1 1 1 1 1]

print(d)
print('')
# [[-1152921504606846976  5764616286638539387]
#  [     140217669779458      703167670357872]]

print(e)
print('')
# [0 0 0 0 0]

print("===== 대각의 값이 1인 배열 =====")

f = np.identity(4, dtype=int)
g = np.eye(4, 4, k=0, dtype=int)

print(f)
print('')
# [[1 0 0 0]
#  [0 1 0 0]
#  [0 0 1 0]
#  [0 0 0 1]]

print(g)
print('')
# [[1 0 0 0]
#  [0 1 0 0]
#  [0 0 1 0]
#  [0 0 0 1]]

i = [[1, 2], [3, 4]]
l = np.linalg.inv(i)
