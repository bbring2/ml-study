import numpy as np

# shape -> (a,b) 일때, a개의 로우와 b개의 컬럼으로 구성된 array
# ndim -> 배열의 차원을 알려준다. 

array1 = np.array([1, 2, 3])
print('array1 type: ', type(array1))
print('array1 array shape: ', array1.shape)
print('array1은 ', array1.ndim, '차원')

array2 = np.array([[1, 2, 3], [3, 4, 5]])
print('array2 type: ', type(array2))
print('array2 array shape: ', array2.shape)
print('array2은 ', array2.ndim, '차원')

array3 = np.array([[3, 2, 1]])
print('array3 type: ', type(array3))
print('array3 array shape: ', array3.shape)
print('array3은 ', array3.ndim, '차원')