def SubArrayWithMaximumSum(arr , b):
    max = float("-inf")
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            output=[]
            for k in range(i,j+1):
                output.append(arr[k])
            intsum = sum(output)
            if intsum > max and intsum <= b:
                max = intsum
                maxArray = output
    print(f"The maximum subArray is {maxArray} and the sum is : {max}")  

arr = list(map(int,input().split()))
b = int(input())
SubArrayWithMaximumSum(arr,b)