# Q5 read a no. it is divisible by 3or its last digit is 4.
Num = int(input("Enter the Number : "))
if (Num%3==0 and abs(Num%10)==4):
    print(Num,"is divisible by 3 and contains 4 at it's last.")
elif (Num%3==0 or abs(Num%10)==4):
    print(Num,"is divisible by 3 and contains 4 at it's last.")
else:
    print(Num,"does'nt divisible by 3 and not contains 4 at it's last.")