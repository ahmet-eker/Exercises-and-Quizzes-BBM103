import math

b = int(input("Please enter b: "))
c = int(input("Please enter c: "))

discrement_value = (b**2)-(4*c)

if discrement_value > 0:
    root1 = (-b + math.sqrt(discrement_value))/2
    root2 = (+b + math.sqrt(discrement_value))/2
    print("Your roots are:",root1,",",root2, sep=' ')
else:
    print("there are no roots")