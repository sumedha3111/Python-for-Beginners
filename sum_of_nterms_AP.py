# Function to calculate sum of n terms in geometric series

def sum_ap(a,d,n):
    
    sum = 0
    i = 0
    while(i< n):
        sum = sum + a
        a = a + d # a is the first term and d is the common difference.
        i = i + 1 # This is like a + ar + ar^2...ar^n.
        #print(a)
    return sum

#driver function
    
#Input values for a,r,n are received from user.

a = input("Enter the first value of the arithmetic series :")
d = input("Enter the common difference of the series :" )
n = input("Enter the number of terms of the series :")


print("\nThe sum of all the terms of the AP is %.5f" %sum_ap(int(a),float(d),int(n))) #prints the sum as output using the sum_gp function
