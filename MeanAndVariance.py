import numpy as np

lst = [] 
n = int(input("Enter the value on N: ")) 
  
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)
x=np.array(lst)
print("\nOriginal array: ")
print(x)
r1 = np.mean(x)
r2 = np.average(x)
assert np.allclose(r1, r2)
print("\nMean: ", r1)
r1 = np.std(x)
r2 = np.sqrt(np.mean((x - np.mean(x)) ** 2 ))
assert np.allclose(r1, r2)
print("\nstd: ", 1)
r1= np.var(x)
r2 = np.mean((x - np.mean(x)) ** 2 )
assert np.allclose(r1, r2)
print("\nvariance: ", r1)

"""
Variance is the variability of model prediction for a given data point or a value which tells us spread of our data
The sample mean is simply the average of all the measurements in the sample. 
"""

