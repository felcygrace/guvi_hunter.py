g=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if(i==l.index(i)):
        s.append(i)
print(*(sorted(s)))
if(len(s)==0):
    print(-1)
