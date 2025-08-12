# Q7 you are given three integer angles of a triangle tell wheather the triangle is valid or not.x
Angle_1 = int (input("Enter the Angle 1 : "))
Angle_2 = int (input("Enter the Angle 2 : "))
Angle_3 = int (input("Enter the Angle 3 : "))
if(Angle_1+Angle_2+Angle_3 == 180):
    print("The tringle is a valid tringle.")
else:
    print("The tringle is'nt a valid tringle.")