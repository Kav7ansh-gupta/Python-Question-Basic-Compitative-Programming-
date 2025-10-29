def SubArrayGoodOrNot(arr , b):
    Good_array = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            output=[]
            for k in range(i,j+1):
                output.append(arr[k])
            intsum = sum(output)
            if (len(output)%2 ==0 and intsum < b) or (len(output)%2 !=0 and intsum > b) :
                Good_array+=1
    return Good_array

arr = list(map(int,input().split()))
b = int(input())
print(SubArrayGoodOrNot(arr,b))