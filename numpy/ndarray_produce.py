import numpy as np

sequence_array = np.arange(2, 11) # 파라미터는 start, stop 해서 배열 바로 생성 가능
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)
print(sequence_array.ndim)

# 파라미터에 튜플 형태의 shape 값을 입력하면 모든 값을 0으로 채운 해당 shape을 가진 ndarray 반환
zero_array = np.zeros((3, 2), dtype='int32')
print(zero_array)
print(zero_array.dtype, zero_array.shape)
print(zero_array.ndim)

# 파라미터에 튜플 형태의 shape 값을 입력하면 모든 값을 1으로 채운 해당 shape을 가진 ndarray 반환
one_array = np.ones((3, 2))
print(one_array)
print(one_array.dtype, one_array.shape)
print(one_array.ndim)
