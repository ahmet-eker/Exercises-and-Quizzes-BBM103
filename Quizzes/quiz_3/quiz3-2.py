import sys

lucky_number_set = [int(i) for i in sys.argv[1].split(",")]

def delete_negatives():
    for number,member in enumerate(lucky_number_set[:]):
        if int(member)<0:
            lucky_number_set.remove(member)

def turn_integer():
    for number,member in enumerate(lucky_number_set[:]):
        lucky_number_set[number]=int(member)

def collective_remove(a):
    delete_liste=[]
    for t in range(len(lucky_number_set[:])):
        if t%a==a-1:
            delete_liste.append(lucky_number_set[t])

    for t in delete_liste:
        lucky_number_set.remove(t)

k=1
for t in range(len(lucky_number_set)):
    a = lucky_number_set[k]
    if a > len(lucky_number_set):
        break
    collective_remove(a)
    if lucky_number_set[k]==a:
        k+=1
print(lucky_number_set)