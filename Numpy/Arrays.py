import numpy as np
# print(np.__version__)

#arr=np.array([1,2,3,4,5]) # 1D
arr=np.array([[1,2,3,4,5],[5,6,7,4,3]]) # 2D
#arr=np.array([[[1,2,3,4,5],[5,6,7,4,3]],[[1,2,3,4,5],[5,6,7,4,3]]]) # 3D

#Index 
#print(arr[2])
#print(arr[0][2])
#print(arr[0][0][2])

#Negative Indexing
#print(arr[-2])
#print(arr[1][-4])
#print(arr[-1,-1,-5])

# Print the dimension of the array.
# print(arr.ndim)

#generate a array with given number of dimensions.
# arr=np.array([1,2,3,4,5],ndmin=6) 


#Slicing
#print(arr[1:3]) #1D
#print(arr[-3:]) #1D negative index
# print(arr[0:2,2]) #2D

#Datatype
print(arr.dtype)




