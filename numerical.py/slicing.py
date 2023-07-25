import numpy as num

arr = num.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
print(arr[2:-2])
print(arr[1:-1:3])


arrd2 = num.array([[1,2,3,4],[1,2,8,4]])
print(arrd2[1, 1:-1])
print(arrd2[0:+1, 2])
print(arrd2[1:4,1:-1])

arrd3 = num.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
print(arrd3[0,1,1:-1])
