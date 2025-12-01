n = int(input())
arr = list(map(int,input().split()))
SumArr = sum(arr)
cost = 0

for i in arr:
    cost += SumArr
    SumArr-= i
    arr.pop(0)
    print(arr)
print(cost)