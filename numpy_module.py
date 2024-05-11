import numpy as np

arr = np.array(([1,2,3,4],[5,6,7,8],[9,10,11,12]))
print(arr.dtype)                               # int32
print(arr.ndim)                                # 3
print(arr.shape)                               # (3,4)
print(arr.itemsize)                            # 4 
print(arr.nbytes)                              # 48
arr[2][1]                                      # 10
arr[0:3:2,0:4:2]                               # [[1,3],[9,11]]
arr.reshape((2,6))                             # [[1,2,3,4,5,6],[7,8,9,10,11,12]]
arr.flatten()                                  # [1,2,3,4,5,6,7,8,9,10,11,12]
ones = np.ones((3,4)); print(ones)             # [[1. 1. 1. 1.],[1. 1. 1. 1.],[1. 1. 1. 1.]]
zeros = np.zeros((3,4)); print(zeros)          # [[0. 0. 0. 0.],[0. 0. 0. 0.],[0. 0. 0. 0.]]
eye = np.eye(3,4); print(eye)                  # [[1 0 0 0],[0 1 0 0],[0 0 1 0]]
diag = np.diag([2,3,4]); print(diag)           # [[2 0 0],[0 3 0],[0 0 4]]
diag = np.diag(([2,4,5],[6,7,8])); print(diag) # [2 7]
arange = np.arange(1,11,2); print(arange)      # [1 3 5 7 9]
linspace = np.linspace(1,10,4); print(linspace)# [1. 4. 7. 10.]


