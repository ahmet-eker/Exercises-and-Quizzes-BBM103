your_email = input("Write your email: ")

def check(mail):
    if "@" and "." in mail:
        return True
    else:
        return False

if check(your_email)==True:
    print("Your email is valid")
elif check(your_email)==False:
    print("Your email is not valid")