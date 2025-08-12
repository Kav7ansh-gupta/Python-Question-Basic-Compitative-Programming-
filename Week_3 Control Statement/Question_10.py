# Q10 Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not
A = int(input("Enter a number : "))

if (A%5 == 0 and A%11 == 0):
    print(A,"id divisible by 5 and 11 both")
else:
    print(A,"is not divisible by nor 5 nither 11.")