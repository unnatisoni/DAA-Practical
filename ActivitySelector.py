s = list(map(int,input().split()))
f = list(map(int,input().split()))
def bubblesort(s,f):
    for i in range(0,len(s)-1):
        for j in range(0,len(s)-1-i):
            if(f[j]>f[j+1]):
                t=f[j]
                f[j]=f[j+1]
                f[j+1]=t
                r= s[j]
                s[j]=s[j+1]
                s[j+1]=r
    return [s,f]
l = bubblesort(s,f)
s = l[0]
f = l[1]
def greed_selector(s,f):
    A=[0]
    k=0
    for i in range(1,len(s)):
        if(s[i]>=f[k]): 
            A.append(i)
            k=i
    return A
res = greed_selector(s,f)
print(res)
