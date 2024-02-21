import random

user_input = int(input("Try to guess the number between 0 - 100: "))

target_number= random.randint(0,100)
while user_input!=target_number:
    if user_input>target_number:
        user_input = int(input("Please decrease your number: "))
    elif user_input<target_number:
        user_input = int(input("Please increase your number: "))

print("Correct!!")