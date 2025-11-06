import numpy as np
# array1 = np.arange(12).reshape(4,3)
# array2 = np.arange(16).reshape(4,4)
# print(array1)
# print(array2)

array1 = np.array([
    [2, 3,4],
    [6,7,2]
     
])

array2 = np.array([
    [1, 0,4],
    [3,1,2]
     
])

# print(array1)
# print(array2)

#ADDITION IN THE NUMPY 
addition =array1 +array2

print("addition of two array in the numpy",addition)


#SUBTRACTION IN THE NUMPY
subtraction = array1 - array2
print("subtraction of two array in the numpt: " ,subtraction)


#MULTIPLICATION IN THE NUMPY
multiplication = array1*2
multiplication2 = array1 *array2
print("multiplication of array1 with scalar value 2 : ", multiplication)
print("Multiplication of two array in the numpy : ",multiplication2)



#DIVISION IN THE NUMPY 
division = array1/10
division2 = array1/array2
print("divsion of two array in the numpy : ",division2)
print("division of the array1 with scalar value 10:" , division)


##MEAN AND MEDIAN IN THE NUMPY 

mean = np.mean(array1)
mean2 = np.mean(array2)

print("mean of the array1 : ",mean)
print("mean of the array2 : " , mean2)

median = np.median(array1)
median2 = np.median(array2)
print("meduim of the array1 : ",median)
print("median of the array2 : ", median2)


##HANDLING THE MISSING VALUE IN THE NUMPY 
ARR = np.array([
    [1,2 ,np.nan],
    [5,7,np.nan]
])
mean_value = np.nanmean(ARR,axis = 1)  #IT IGNORE THE NAN VALUE WHILE CALCULATING THE MEAN

print(mean_value)

median_value = np.nanmedian(ARR, axis=0)  #IT IGNORE THE NAN VALUE WHILE CALCULATIG THE MEDIAN

print(median_value)

##1 indicates row wise operation 
##0 indicates column wise operation
