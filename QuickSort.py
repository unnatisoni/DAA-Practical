def quickSort(A,p,r):
    if p<r:
        q = Partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

def Partition(A,p,r):
    x = A[r]
    i=p-1
    for j in range(p,r):
        if(A[j] <= x):
            i=i+1 
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1 

A = [9,6,5,3,7,1]
quickSort(A,0,len(A)-1)
print(A)
        
