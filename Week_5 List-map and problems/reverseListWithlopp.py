my_list = [1,2,3,4,5]
n=len(my_list)
for i in range(0,n//2):
    my_list[i],my_list[n-1-i]=my_list[n-1-i],my_list[i]
print(my_list)