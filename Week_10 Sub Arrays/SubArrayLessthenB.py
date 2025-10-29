def SubArrayLessthenB(arr , b):
    count = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            output=[]
            for k in range(i,j+1):
                output.append(arr[k])
            intsum = sum(output)
            if intsum <b:
                count+=1
    return count

arr = list(map(int,input().split()))
b = int(input())
print(SubArrayLessthenB(arr,b))