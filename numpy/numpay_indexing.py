# 단일값 추출하기
import numpy as np

array1 = np.arange(1, 10)
print('array1: ', array1)

value = array1[2]
print(value)
print(type(value))

array1d = np.arange(1, 10)
array2d = array1d.reshape(3, 3)
print(array2d)

# 1차원 슬라이싱
array2 = np.arange(1, 10)
array4 = array2[:3]
print(array4)

array3 = array2[3:]
print(array3)

array5 = array2[:]
print(array5)

# 2차원 슬라이싱
# 콤마로 로우와 컬럼 인덱스를 지칭하는 부분만 다르다
array1d1 = np.arange(1, 10)
array2d1 = array1d1.reshape(3, 3)
print('array2d1: \n', array2d1)

print('array2d2[0:2, 0:2]\n', array2d1[0:2, 0:2])
print('array2d2[1:3, 0:3]\n', array2d1[1:3, 0:3])
print('array2d2[1:3, :]\n', array2d1[1:3, :])
print('array2d2[:, :]\n', array2d1[:, :])
print('array2d2[:2, 1:]\n', array2d1[:2, 1:])
print('array2d2[:2, 0]\n', array2d1[:2, 0])

# 팬시 인덱싱
#