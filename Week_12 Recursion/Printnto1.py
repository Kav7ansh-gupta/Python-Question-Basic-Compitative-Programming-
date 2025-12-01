def Print1toN(n):
    if n ==0:
        return
    print(n)
    Print1toN(n-1)
n = int(input())
Print1toN(n)
    