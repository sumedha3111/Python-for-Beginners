def calculate_lcm(s, n):

   # choose the greater number
   if s > n:
       greater = s
   else:
       greater = n

   while(True):
       if((greater % s == 0) and (greater % n == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 50
num2 = 20

print("The L.C.M. is", compute_lcm(num1, num2))