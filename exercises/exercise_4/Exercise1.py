n = int(input("Enter a number: "))

sum_even = 0
sum_odd = 0
for t in range(1,n+1):
    if t%2==0:
        sum_even+=t
    elif t%2==1:
        sum_odd+=t

average_of_even = sum_even/(n//2)

print("The sum of odd numbers is {}".format(sum_odd))
print("The average of even numbers is {}".format(average_of_even))