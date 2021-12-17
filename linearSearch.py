l = list(map(int,input("Enter the array").split()))
n = int(input("Enter the value to be searched in the array"))
c=0
for i in l:
 if(i == n):
     c=1
     print("Element Found")
     break
if(c==0):
 print("Element not found") 
