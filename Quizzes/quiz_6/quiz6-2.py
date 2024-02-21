import sys

input_value = int(sys.argv[1])

my_list = [" "*(input_value-i) + (2*i-1)*"*" if i <= input_value else " "*(i-input_value) + (2*(input_value-(i-input_value))-1)*"*" for i in range(1,2*input_value)]

for t in my_list:
    print(t)

#Ahmet Şeref Eker
#2210356098
#Hacettepe Universtiy