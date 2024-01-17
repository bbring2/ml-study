# reshape() 메서드는 ndarray를 특정 차원 및 크기로 변환되는 메서드
# 단, reshape() 메서드는 지정된 사이즈로 변경이 불가능하면 에러를 뱉는다
# -1을 파라미터로 사용하게 되면, 원래 ndarray와 호환되는 새로운 shape으로 변환해준다.

import numpy as np

array1 = np.arange(10)
print('array1: \n', array1)

array2 = array1.reshape(2, 5)
print('array2: \n', array2)

array3 = array1.reshape(5, 2)
print('array3: \n', array3)

array4 = array1.reshape(-1, 5)
print('array4 shape: ', array4.shape)

array5 = array1.reshape(5, -1)
print('array5 shape: ', array5.shape)

array6 = np.arange(8)
array3d = array6.reshape((2, 2, 2))
print('array3d: \n', array3d.tolist())

# 3차원 ndarray를 2차원 ndarray로 변환
array7 = array3d.reshape(-1, 1)
print('array7: \n', array7.tolist())
print('array7 shape: ', array7.shape)

# 1차원 ndarray를 2차원 ndarray로 변환
array8 = array6.reshape(-1, 1)
print('array8: \n', array8.tolist())
print('array8 shape: ', array8.shape)