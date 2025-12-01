def FactorialOfNnumber(n):
    if n == 0:
        return 1
    return (FactorialOfNnumber(n-1)*n)

print(FactorialOfNnumber(8))