import numpy as np 
import math 
a = [0,1,2,3,4,5,6,7,8,9]
b = [1,3,2,5,7,8,8,9,10,12]

#Changing lists to numpy arrays
x = np.array(a)
y = np.array(b)

#Finding b0 and b1
mean_x = np.mean(x)
mean_y = np.mean(y)
SS_xy = np.sum(y*x) - 10*mean_y*mean_x 
SS_xx = np.sum(x*x) - 10*mean_x*mean_x 

b_1 = SS_xy / SS_xx 
b_0 = mean_y - b_1*mean_x 
print("\nRegression Coefficients: b0 = ",b_0," b1 = ",b_1)

#Finding SSR,SST,SSE and R squared
for i in range(10):
    y_pred = b_0 + b_1*x
SSR = 0
SSE = 0
for i in range(10):
    SSR = SSR + math.pow((y_pred[i]-mean_y),2)
    SSE = SSE + math.pow((y[i]-y_pred[i]),2)
print("\nSSR = ",SSR)    
print("\nSSE = ",SSE)
SST = SSR +SSE
R_squared = SSR/SST
print("\nR squared = ",R_squared)


#Gradient decent full batch

print("\nGRADEIENT DECENT")
bb0=0
bb1=0
a=0.001
n=10
y_exp=np.zeros(n)
for j in range(10000):
    for i in range(n):
        y_exp[i]=b_0+b_1*x[i]
        bb0=bb0+a*(y[i]-y_exp[i])
        bb1=bb1+a*(y[i]-y_exp[i])*x[i]
print("\nB0=",bb0)
print("B1=",bb1)
 

#Gradient decent Stochastic
print("\nGRADEIENT DECENT Stochastic")
bb0=0
bb1=0
a=0.001
y_exp=np.zeros(n)
b=[0,0]
se=10
while(se>1):
    for i in range(n):
        y_exp[i]=b_0+b_1*x[i]
        bb0=bb0+a*(y[i]-y_exp[i])
        bb1=bb1+a*(y[i]-y_exp[i])*x[i]
        b[0]=bb0
        b[1]=bb1
    e=y-y_exp
    se=np.sum((e**2))*(1/n)
print("\nSquared error=",se)
print("B0=",bb0)
print("B1=",bb1)




    

