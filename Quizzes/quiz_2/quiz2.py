import sys

def healthStatus(height, mass):
    bmi = float(mass)/(float(height)**2) #body mass index calculating
    if bmi>=30:
        return "obese"
    elif bmi>=24.9:
        return "overweight"
    elif bmi>=18.5:
        return "healthy"
    else:
        return "underweight"

try:
    a  = int((int(sys.argv[1])*2)+(int(sys.argv[2])*3)+int(sys.argv[3]))  #calculating the total points
    print(a)  #printing only the integer
except IndexError:
    pass
except NameError:
    pass
except ValueError:
    pass

#Ahmet Şeref Eker
#Hacettepe Computer Engineering
#2210356098