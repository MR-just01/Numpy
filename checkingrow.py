# checking the presence of a row using tolist()


# ndarray.tolist()

# Parameters: None -> tolist() does not take any parameters.
# Returns: A nested Python list containing all array elements.
import numpy as np
arr = np.array([[1,2],
                [3,4]])
row = [3,4]
print(row in arr.tolist())

arr1 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15],
                 [16,17,18,19,20]])
print("Array is :\n " , arr1)

print([1,2,3,4,5] in arr1.tolist())
print([11,12,13,14,15] in arr1.tolist())
print([-1,2,3,4,5] in arr1.tolist())
print([11,22,13,24,25] in arr1.tolist())

