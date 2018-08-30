import numpy as np


#numpy

x = np.ones(10)

print(x) #size = (1*10)

y = np.zeros((3,4))

print(y) #size = (10*10)

x_random = np.random.randn(3,6) #random value matrix

print(x_random)

# for loop 
i = [1,2,3,4,5,6,7,8,9,10]
out = [in_data**2 for in_data in i] 
print(out)

# if 
for j in range (10):
	if j**2 <=10:
		print(out[j])
	else:
		print('j**2 >10')