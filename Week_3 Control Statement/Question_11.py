# Q11 WAP to check whether a year is a leap year or not.
Year = int(input("Enter the Year : "))

if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
        print(Year,("is a leap Year"))
else:
        print(Year,("is'nt a leap Year"))
    
        