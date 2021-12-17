def selectionSort(A):
    for i in range(len(A)):
        min_index = i 
        for j in range(i+1,len(A)):
            if(A[j]<A[min_index]):
                min_index = j 
        A[i],A[min_index] = A[min_index],A[i]

A = [8,5,3,6,2,9]
selectionSort(A)
print(A)
