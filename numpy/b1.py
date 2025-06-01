#script import numpy
import numpy as np

# Create a object numpy array, save in disk and easy to query it
a = np.array([1,2,3,4,5])

print(a) 
print(np.__version__)
print(type(a))


#0-D array
b = np.array(42)
print(b)
print(b.ndim)

#two arrays
c = np.array([[1,2,3], [4,5,6]])
print(c)
print(c.ndim)

#three arrays 

d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(d)
print(d.ndim)

# 3-D array with two 2-D arrays,
e = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(e)
print(e.ndim)

#verify the dim of array
array = np.array([1,2,3,4,5], ndmin = 5)
print(array.ndim)