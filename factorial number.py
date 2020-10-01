def factorial(p): 
    if p< 0: 
        return 0
    elif p == 0 or p == 1: 
        return 1
    else: 
        fact = 1
        while(p > 1): 
            fact *= p
            n -= 1
        return fact 