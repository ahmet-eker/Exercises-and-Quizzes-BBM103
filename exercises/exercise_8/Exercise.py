import sys

# example input:
# python3 Exercise.py 1,2,3,4,5,6,7,8,9

my_list = sys.argv[1].split(",")
b = len(my_list)


def maximum(a):
    if len(a) !=1:
        if max(a[0],a[1]) == a[1]:
            return maximum(a[1:])
        elif max(a[0],a[1]) == a[0]:
            a.pop(1)
            return maximum(a)
    else:
        return a[0]

def minimum(a):
    if len(a) !=1:
        if min(a[0],a[1]) == a[1]:
            return minimum(a[1:])
        elif min(a[0],a[1]) == a[0]:
            return minimum([a[0]]+a[2:])
    else:
        return a[0]

def average(a):
    if len(a) == 1:
        return int(a[0])/b
    else:
        return (int(a[0])/b + average(a[1:]))

if abs(round(average(my_list)) - average(my_list)) < 0.00000000001:
    average_value = round(average(my_list))
else:
    average_value = (average(my_list))

print("Max value is :",maximum(my_list))
print("Min value is :",minimum(my_list))
print("Average value is :",average_value)

#Ahmet Şeref Eker
#Hacettepe Bilgisayar Mühendisliği
#2210356098
