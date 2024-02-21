the_year = int(input("Enter the year: "))
if the_year % 4 == 0 and the_year % 100 !=0 or the_year % 400 == 0:
    print("The yaer {} is a leap year".format(the_year))
else:
    print("The year {} is not a leap year".format(the_year))