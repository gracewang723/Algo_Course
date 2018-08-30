import numpy as np
'''
Fibonacci squence
'''

#the length of squence
n = 20 
#def the sequence
f_squence = [1]*n 
#cal the sequence

for count in range(2,n): #change numbers from the 3rd
	f_squence[count] = f_squence[count-1] + f_squence[count-2]

print('sequen length : ',n)
print('Fibonacci sequence : ',f_squence) 
print('avg of squence : ',np.mean(np.array(f_squence)))
print('min of squence : ',np.min(np.array(f_squence)))
print('max of squence : ',np.max(np.array(f_squence)))
print('std of squence : ',np.std(np.array(f_squence)))
print('variance of squence : ',np.var(np.array(f_squence)))