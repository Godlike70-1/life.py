import numpy as np

array = np.array([1,2,3])
print(array[0]+array[1])

ary = np.array([[4,5,6],[7,8,9]])
print(ary[0,1])
print(ary[1,2])


three = np.array([[[10,11,12],[13,14,15]],[[16,17,18],[19,20,21]]])
print(three[1,1,-1])
