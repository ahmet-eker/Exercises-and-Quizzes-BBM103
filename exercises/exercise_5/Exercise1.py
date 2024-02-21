number = int(input("Enter a nummber: "))


my_dict = {i: "*" * i for i in range(1,number+1)}

for a in range(1,number+1):
    print(my_dict[a])
