def binarySearch(arr, ele, l, r):
    if(r>=l):
         mid = (l+r) //2
         if(arr[mid] == ele):
             return mid
         elif(arr[mid]<ele):
             return binarySearch(arr,ele,mid+1,r)
         else:
             return binarySearch(arr,ele,l,mid-1)
    else:
        return -1 

arr = list(map(int,input().split()))
ele = int(input())

res = binarySearch(arr,ele,0,len(arr))
if(res == -1):
    print("Element not found")
else:
    print("Element found at index => ",res)


