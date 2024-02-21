import sys

base = int(sys.argv[1])
power = int(sys.argv[2])

result1 = pow(base,power)
print(" {}^{} = {}".format(base,power,result1),end=" = ")

sum = 0
for a,character in enumerate(str(result1)):
    sum+=int(character)
    print(character,end="")
    if a+1 !=len(str(result1)):
        print(" + ",end="")

print(" =",sum)