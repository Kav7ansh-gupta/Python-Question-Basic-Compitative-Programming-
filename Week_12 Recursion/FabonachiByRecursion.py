def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def printFibonacci(n, current=0):
    if current > n:
        return
    print(fib(current),end=" ")
    printFibonacci(n, current + 1)
r
printFibonacci(6)
