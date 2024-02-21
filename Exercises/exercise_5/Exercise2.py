n = int(input("Enter the n: "))

input = input("Please enter a list with spaces: ")
number_list = input.split(" ")

for t in range(len(number_list)):
    number_list[t] = int(number_list[t])
    
print("My list:",number_list)
number_list.sort(reverse=True)

print("My sorted list:",number_list)
print(f"{n}th largest element of the list:",number_list[n-1])
