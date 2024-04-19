import numpy as
np a = np.array ([1, 2, 3, 4, 5])
print("1D array:")
print (a)
print () b = np.array ([[1, 2, 3], [4, 5, 6]])
print ("2D array:") 
print(b) 
print() 
print("Accessing elements of an array:")
print (a[0]) 
print(b[1, 2]) 
print ()
print("Array slicing:")
print (a[1:4])
print (b[:, 1])
print ()
print ("Array arithmetic:")
c = a + b
print(c)
print() 
print ("Array multiplication:")
d = np.array ([[1, 2], [3, 4]])
e = np.array ([[5, 6], [7, 8]]) f = np.dot (d, e)
print (f)
print()

print("Array shape and size:") print(a.shape) print(b.shape) print(a.size) print(b.size)

