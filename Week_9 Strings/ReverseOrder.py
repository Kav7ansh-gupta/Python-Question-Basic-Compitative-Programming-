str = list(map(str,input().split()))
for i in range(1,len(str)+1):
    print(str[(len(str)-i)],end=" ")

