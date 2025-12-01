arr = list(map(int, input().split()))
n = len(arr)
arr.sort()

for i in range(n):
    if arr[i] == i:
        print("Noble Element is :", arr[i])