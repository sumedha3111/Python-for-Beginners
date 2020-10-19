#program to find whether a no. is shy no. or not

ch=1                               #initialiing the choice variable with 1

while ch ==1:
      s=0                                #initializing sum of digits as 0

      p=1                                #initializing product of digits as 1


      n=int(input("Enter a Number:"))    #Taking input the user given no.
      org=n                              # storing the original no. for further use

      while n!=0 :                       #while loop until the number becomes 0
            r=n%10                       #finding the last digit of the number
            n=n//10                      #eliminating the last digit
            s= s+r                       # finding the sum of the obtained digits
            p=p*r                        # finding the product of the obtained digits
            

            
      if s==p :                          #checking if the sum and product are equal or not
            print(org,"is a shy number :)")
      else :
            print(org, "is not a Shy number :( ")

      ch=int(input(" Wanna try another one?.... Press 1 if yes " ))
            
              
