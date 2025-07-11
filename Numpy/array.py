import numpy as np

arr = np.array([1,2,3,4])
print(arr)
print(np.sum(arr)) #sum
print(np.mean(arr))      # Average → 3.0
print(np.max(arr))       # Largest → 5
print(np.min(arr))       # Smallest → 1
print(np.sqrt(arr))      # Square roots

#multidimentional

matrix = np.array([[1,2],[3,4]])
print(matrix)

print(matrix.shape)
new_matrix = np.reshape(matrix,(4,1))
print(new_matrix*2)

