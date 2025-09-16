arr = list(map(int,input().split()))
odd = []
even = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else :
        odd.append(i)
print(odd)
print(even)