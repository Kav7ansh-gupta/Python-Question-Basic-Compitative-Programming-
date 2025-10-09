n = int(input())

for i in range(n):
    char = chr(65+i)
    for i in range(i+1):
        print(char, end=" ")
    print()