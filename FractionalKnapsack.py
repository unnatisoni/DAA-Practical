p = list(map(int,input().split()))
w=list(map(int,input().split()))
pw = [0 for i in range(len(p))]
for i in range(len(p)):
    pw[i]= p[i]/w[i]
def bubblesort(p,w,pw):
    for i in range(0,len(p)-1):
        for j in range(0,len(p)-1-i):
            if(pw[j]<pw[j+1]):
                t=pw[j]
                pw[j]=pw[j+1]
                pw[j+1]=t
                r=p[j]
                p[j]=p[j+1]
                p[j+1]=r
                q=w[j]
                w[j]=w[j+1] 
                w[j+1]=q
    return [p,w,pw]
l = bubblesort(p,w,pw)
p = l[0]
w = l[1]
pw = l[2]
x=[0 for i in range(len(p))]
M=25
for i in range(len(p)):
    if(w[i]>M):
       break
    x[i]= 1
    M=M-w[i]
if(i<=len(p)):
    x[i]=M/w[i]
ans =0
for i in range(len(x)):
    ans =ans+(x[i]* p[i])
print(ans)
