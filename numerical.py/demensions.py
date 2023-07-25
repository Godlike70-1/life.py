import numpy

zero_dimension = numpy.array(100)
print(zero_dimension,'zero dimension')
one_dimension = numpy.array([1,2,3,4])
print(one_dimension,"one dimension")
two_dimension = numpy.array([[1,2,3],[4,5,6]])
print(two_dimension,"two dimension ")
three_dimension = numpy.array([[[1,2,3],[2,3,4]],[[3,4,5],[4,5,6]]])
print(three_dimension,'three dimensions')

print(zero_dimension.ndim)
print(one_dimension.ndim)
print(two_dimension.ndim)
print(three_dimension.ndim)

arr = numpy.array([1,2,3,4], ndmin=4)
print(arr)
print(arr.ndim)