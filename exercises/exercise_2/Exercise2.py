number = int(input("Please enter a number: "))
answer = 0

for t in range(20):
    
    if number%2==1:
        number//=2
        answer += 10**t
    else:
        number//=2
    
    if number ==0:
        break

print(answer)