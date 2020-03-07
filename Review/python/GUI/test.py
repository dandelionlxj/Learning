
a=input().split()
result=[]
count=1
for i in range(len(a)):
    if a[i+1]==a[i]:
        count+=1
        now=a[i]
    else:
        count=1
        now=a[i]
        result.append(str(count)+str(now))

