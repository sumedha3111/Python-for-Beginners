def search(arr, x):
  for i in range(len(arr)): 
    if arr[i] == x: 
      return i 
  return -1
  
no_inp=input("Enter the number of elements in the list: ")
arr=[]
for i in range(np_inp):
  arr[i]=input()
x=input("Enter the element you want to search: ")
print(search(arr,x))
