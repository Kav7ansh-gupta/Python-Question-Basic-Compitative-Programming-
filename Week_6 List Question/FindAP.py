arr = list(map(int, input().split()))

n = len(arr)

d = abs(arr[0] - arr[1])

for i in range(1, n):
    if abs(arr[i] - arr[i - 1]) != d:
        print("Not an AP")
        break
else:
    print("AP with common difference :", d) 