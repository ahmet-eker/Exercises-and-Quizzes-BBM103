s = int(input("Enter an integer: "))


my_dict = {i: "*" * i for i in range(1,s+1)}
for k in my_dict.values():
    print(k)