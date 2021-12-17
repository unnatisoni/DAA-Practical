l = list(map(int,input("Enter the array").split()))
for i in range(len(l)):
 for j in range(len(l)-1-i):
     if(l[j]>l[j+1]):
         l[j],l[j+1] = l[j+1],l[j]
print(l)
