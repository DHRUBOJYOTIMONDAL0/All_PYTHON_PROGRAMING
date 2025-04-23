import numpy as np
# # print(np.__version__)

# l = [1,2,3,4,5] # numpy array is homogeneous
# l = [1,2,3,4,5,"Dhrubo"]
# arr = np.array(l) # convert to array(first way )
# print(arr)
# print(type(arr))  # nd stands for n-dimensional

# more way to convert array



# l = [1,2,3,4,5]
# # arr = np.asarray(l) # second way
# arr = np.asanyarray(l) # Third way
# # arr[0] = 100 # change the value
# print(arr)
# print(type(arr))
# print("The elements is ", arr[0])  # Example of accessing an element with a valid index

# b = arr.copy() # copy array 
# print(b)

# s = np.fromfunction(lambda i,j : i==j, (3,3))
# arr = s.ndim
# arr1 = s.shape # SHAPE OF ARRAY
# arr2 = s.size # number of elements of array
# print(s)
# print(arr)
# print(arr1)
# print(arr2)

# s = np.fromfunction(lambda i, j: i*j, (3,3))
# print(s)

# for i in range(5):
#     print(i)

# s = np.fromstring("23 24 25", sep = " ", dtype = int)
# print(s)

# string = "Dhrubo, Senha, Liza"
# string1 = string.split(",")
# print(string1)

# s = np.arange(1, 10, 0.1)
# print(s)

s = np.linspace(1,5, 10)
print(s)