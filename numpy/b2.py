import numpy as np 
#dim = 1
arr_dim1 = np.array([1,2,4,5,6])
print(arr_dim1[0])
print(arr_dim1[0:3])
print(arr_dim1[1] + arr_dim1[2])

#dim = 2
arr_dim2 = np.array([[1,2,3], [4,5,6]])
print(arr_dim2[1,1])

#dim = 3 
arr_dim_3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_dim_3[0, 1, 2])
#Use negative indexing to access an array from the end
print(arr_dim_3[0, -1, -2])  # Access the last element of the second array in the first 2-D array