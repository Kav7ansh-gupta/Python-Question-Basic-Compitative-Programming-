# Q12 WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc
Day = int(input("Enter a number Between 1 to 7 : "))

match Day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")