import numpy as np
import math
lst1 = []
lst2= []
n = int(input("Enter the value of n :"))
for i in range(0,2):
	for j in range(0,n):
		if i==0:
			ele = int(input())
			lst1.append(ele)
		if i==1:
			ele = int(input())
			lst2.append(ele)
x = np.array(lst1)
y = np.array(lst2)
print("\nOriginal array1:")
print(x)
print("\nOriginal array2:")
print(y)
print("\nCovariance matrix of the arrays:\n",np.cov(x, y))
print("\nCorrelation matrix of the arrays:\n",np.corrcoef(x, y))