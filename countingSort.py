def countingSort(A,k):
    c = [0 for i in range(k+1)]
    b = [0 for i in range(len(A)+1)]
    for i in A:
        c[i] = c[i]+1 
    for i in range(1,len(c)):
        c[i] = c[i]+c[i-1]
    for i in range(len(A)):
        b[c[A[i]]] = A[i]
        c[A[i]] = c[A[i]]-1 
    return b 

A = [9,6,5,3,7,1]
res = countingSort(A,max(A))
print(res[1:])
        
