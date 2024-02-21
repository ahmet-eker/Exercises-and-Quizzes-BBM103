import sys

input = int(sys.argv[1])
last = (input*2)-1

def recursion(x):
    if x == last:
        return " "*(input-1) + "*"
    elif x>input:
        return " "*(x-input) + (2*(input-(x-input))-1)*"*" + "\n" + recursion(x+1)
    elif x <= input:
        return " "*(input-x) + (2*x-1)*"*" + "\n" + recursion(x+1)
print(recursion(1))

#Ahmet Şeref Eker
#2210356098
#Hacettepe Universtiy