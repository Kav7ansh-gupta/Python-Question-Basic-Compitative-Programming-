arr = list(map(int,input().split()))

uni = 0

for i in arr:
    uni ^= i
print(uni)