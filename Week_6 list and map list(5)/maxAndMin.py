arr = list(map(int,input().split()))
max = float("-inf")
min = float("inf")

for i in arr:
    if i > max :
        max = i
    if i < min :
        min = i
print(f"The minimum value in array is {min} and maximum is {max}.") 