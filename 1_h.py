n=int(input())
l=input().split()
l1=[]
for i in range(n):
  for j in range(i+1,len(l)):
    if l[i]==l[j]:
         l1.append(l[i])
if len(l1)==0:
  print('unique')
else:
  l1.sort()
  d=set(l1)
  for i in d:
    print(l1,end='')
