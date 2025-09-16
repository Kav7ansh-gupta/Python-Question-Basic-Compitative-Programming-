arr = list(map(int,input().split()))
reversedArr=[]

for i in range(len(arr)):
    reversedArr.append(arr[(len(arr)-1)-i])
print(reversedArr)