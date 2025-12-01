arr = list(map(int, input().split()))
n = len(arr)
max_value = float('-inf')

for i in range(n):
    for j in range(n):
        if 