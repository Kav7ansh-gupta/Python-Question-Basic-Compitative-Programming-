n = int(input())
arr = list(map(int,input().split()))
passed = 0
failed = 0

for i in arr:
    if i >=35 :
        passed+=1
    else:
        failed+=1
print(f"{passed} {failed}")