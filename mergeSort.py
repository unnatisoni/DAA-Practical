def mergeSort(A,p,r):
    if p<r:
        q = (p+r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    n1 = q-p+1 
    n2 = r-q
    l1 = [0]*(n1+1) 
    l2 = [0]*(n2+1)
    for i in range(n1):
        l1[i] = A[p+i]
    for i in range(n2):
        l2[i] = A[q+i+1]
    i=0
    j=0
    k=p
    while(i<n1 and j<n2):
        if(l1[i]<l2[j]):
            A[k] = l1[i]
            i=i+1 
        else:
            A[k] = l2[j]
            j=j+1 
        k = k+1 
    while(i<n1):
        A[k] = l1[i]
        i=i+1 
        k=k+1 
    while(j<n2):
        A[k] = l2[j]
        j=j+1 
        k=k+1 
    
A = [5,4,3,2,1]
mergeSort(A,0,len(A)-1)
print(A)
    


        
