def Print1toN(n):
    if n ==0:
        return
    Print1toN(n-1)
    print(n)
n = int(input())
Print1toN(n)
    