import numpy as np

arr = np.array([[1,2,34],
                [41,np.nan, np.nan]])

print("original array : \n",arr)

print("Removing all non-numeric values: ")
cleaned_arr = arr[~np.isnan(arr).any(axis =1)]
print(cleaned_arr)



n_arr1 = np.array([[10.5, 22.5, 3.8, 5],
                  [23.45, 50, 78.7, 3.5],
                  [41, np.nan, np.nan, 0],
                  [20, 50.20, np.nan, 2.5],
                  [18.8, 50.60, 8.8, 58.6]])

print("original array : \n",n_arr1)

print("Removing all non-numeric values: ")
cleaned_arr1 = n_arr1[~np.isnan(n_arr1).any(axis =1)]
print(cleaned_arr1)