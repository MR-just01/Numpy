import numpy as np 

# randomnumgen = np.random.default_rng(seed=1)
# print(randomnumgen.integers(low = 10,high = 30 ,size=(4,3)))
#when we want the same array over again so we will use the seed method 


##float method 
# print(np.random.uniform(low = 1,high = 8, size=(2,3)))

# how to randomly shuffle the array 
# rng = np.random.default_rng()
# array = np.array([1,23,45,556,324 ])
# rng.shuffle(array)
# print(array)

## how to get the random choice 
rngs = np.random.default_rng()
fruits = np.array(['🍎' , '🍍' , '🍒' ,'🍓'])
fruit = rngs.choice(fruits,size=(2,2))
print(fruit)