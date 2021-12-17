def insertionSort(A):
    for i in range(1,len(A)):
        key = A[i]
        j=i-1
        while(j>=0 and A[j]>key):
            A[j+1] = A[j]
            j=j-1 
        A[j+1] = key
A = [8,5,3,6,2,9]
insertionSort(A)
print(A)
