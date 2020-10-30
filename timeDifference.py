def difference(h1, m1, h2, m2): 
      
    # convert h1 : m1 into 
    # minutes 
    t1 = h1 * 60 + m1 
      
    # convert h2 : m2 into 
    # minutes  
    t2 = h2 * 60 + m2 
      
    if (t1 == t2):  
        print("Both are same times") 
        return 
    else: 
          
        # calculating the difference 
        diff = t2-t1 
          
    # calculating hours from 
    # difference 
    h = (int(diff / 60)) % 24
      
    # calculating minutes from  
    # difference 
    m = diff % 60
  
    print(h, ":", m) 
  
if __name__ == "__main__": 
      
    difference(7, 20, 9, 45) 
    difference(15, 23, 18, 54) 
    difference(16, 20, 16, 20) 
