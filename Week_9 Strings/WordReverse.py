str = list(map(str,input().split()))

for i in range(len(str)):
    temp = str[i]
    n= len(temp)
    for j in range(1,n+1):
        print(temp[n-j],end="")
    print(end=" ")