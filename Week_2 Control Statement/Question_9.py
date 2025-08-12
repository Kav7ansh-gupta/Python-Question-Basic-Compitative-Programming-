# Q9 Accept the percentage from user and desplay the grades acording to criteria.
num = int(input("Enter Your Grade in percentage : "))
if num > 90 :
    print("Grade : O")
elif num > 80 :
    print("Grade : A")
elif num > 70 :
    print("Grade : B")
elif num > 60 :
    print("Grade : C")
elif num > 50 :
    print("Grade : F")