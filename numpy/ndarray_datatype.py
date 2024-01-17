import numpy as np

list1 = [1, 2, 3, 4, 5, 6]
print(type(list1))
array1 = np.array(list1)
print(type(array1))
print(array1, array1.dtype)

array_int = np.array([1, 2, 3])
array_float = array_int.astype('float64')
print(array_float, array_float.dtype)

array_int1 = array_float.astype('int32')
print(array_int1, array_int1.dtype)

array_float1 = np.array([1.6, 2.6, 3.1])
array_int2 = array_float1.astype('int32') # astype으로 float -> int 변환시 반올림이 아닌 버림
print(array_int2, array_int2.dtype)