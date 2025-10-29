def SubArrayGoodOrNotHard(arr):
    finalSum = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            output=[]
            for k in range(i,j+1):
                output.append(arr[k])
            intsum = 0
            for value in output:
                intsum+=value
            finalSum+=intsum
    return finalSum
def SumOfSubArraysSumEasy(arr):
    n = len(arr)
    ans = 0
    for i in range(0,n):
        total = (i+1)*(n-i)
        contribution = total*arr[i]
        ans+=contribution
    return ans

arr = list(map(int,input().split()))
print(SumOfSubArraysSumEasy(arr))
