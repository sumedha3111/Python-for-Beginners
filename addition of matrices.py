# Program to add two matrices using nested loop

X = [[16,71,33],
    [14 ,15,60],
    [71 ,81,99]]

Y = [[55,8,1],
    [6,17,3],
    [4,5,92]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterates along the rows
for i in range(len(X)):
   # iterates along the columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)