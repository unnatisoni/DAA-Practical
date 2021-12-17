
l=list(map(int,input().split()))
n=len(l)
def heapify(A,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if(l<n and A[l]>A[i]):
       largest=l
    if(r<n and A[r]>A[largest]):
        largest=r
    if(largest!=i):
        A[i],A[largest]=A[largest],A[i]
        heapify(A,n,largest)

def buildHeap(A):
    n=len(A)
    for i in range((n//2)-1,-1,-1):
        heapify(A,n,i)


def heapSort(A):
    n=len(A)
    buildHeap(A)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,i,0)
heapSort(l)
print(l)
