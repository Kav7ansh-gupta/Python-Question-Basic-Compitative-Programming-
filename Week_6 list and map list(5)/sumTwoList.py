arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
outputList = []

for i in range(len(arr1)):
    outputList.append(arr1[i]+arr2[i])
print(outputList)