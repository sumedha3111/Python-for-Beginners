def factorial(p): 
    if p< 0: 
        return 0
    elif (p == 0) or (p == 1):
        return 1
    else: 
        fact = 1
        while(p > 1): 
            fact *= p
            p-= 1
        return fact 
    

# recursive approach to find factorial.
# recursion is a useful tool in mainly functional-programming languages. A function is called again and again to evaluate statements. Useful and powerful.

def factorial(num): 
    if num == 1:    # make a base condition so that the function doesn't go to negative indexes.
        return 1
    else:
        return (num*factorial(num-1))   # the same function will be run against the number.

number  = int(input("Enter a number for factorial.\t"))

print(factorial(number))
