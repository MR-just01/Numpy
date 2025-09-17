##scalar airthmetic 

import numpy as np 
arr = np.array([1.01,2.9,3.99])

# print(arr + 1)
# print(arr-2)
# print(arr *3)
# print(arr/2)
# print(arr**4) #power to the number ** operator used for power



#vector math functio 

# print(np.sqrt(arr))
# print(np.round(arr)) #function used for the roundin up the number in decimal 

# print(np.floor(arr)) # function used to round down the values 
# print(np.pi)

#EXERCISE 
# area of the circle 
# radii = np.array([1,2,3])
# print(np.pi*radii**2)


# #Elementwise arithmetic 

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# print("addition" , arr1+arr2)
# print("subtraction :" ,arr1 -arr2)
# print("Multiplication : " ,arr1*arr2)
# print("division : " ,arr1/arr2)
# print("remainder: ",arr1%arr2)
# print(" power : " ,arr1**arr2)


##comparison operator
marks = np.array([45,56,75,12,67,100,90])
print(marks == 100)
print(marks >=100)
print(marks<=60)
marks[marks<60] = 0
print(marks)
