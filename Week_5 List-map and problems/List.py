My_list = [33,79.9,"Kavyansh gupta",["bca",True]]
# index ----- [0,1,2,3(0,1)]
print(My_list)
print("Name oF the student ", My_list[2])
print("nickName oF the student ", My_list[2][0:5])
print("RollNUmber oF the student ", My_list[0])
print("Marks of the student ", My_list[1])

My_list[1]=80
print("Updated Marks of the student ", My_list[1])
My_list.append(20)
print(My_list)