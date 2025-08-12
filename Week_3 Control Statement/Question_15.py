# Q15 Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle).
Angle_1 = int (input("Enter the Angle 1 : "))
Angle_2 = int (input("Enter the Angle 2 : "))
Angle_3 = int (input("Enter the Angle 3 : "))
if(Angle_1+Angle_2+Angle_3 == 180):
    if (Angle_1== 90 or Angle_2== 90 or Angle_3 == 90 ):
        print("Triangle is a right angle triangle")
    elif(Angle_1 > 90 or Angle_2 > 90 or Angle_3 > 90):
        print("Triangle is a Obtuse angle triangle")
    else:
        print("Triangle is a Acute angle triangle")
else:
    print("The tringle is'nt a valid tringle.")