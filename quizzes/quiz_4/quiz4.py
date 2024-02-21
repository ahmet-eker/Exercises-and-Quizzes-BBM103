import sys

output_file = open("output.File.txt","w") # create or openning output file

with open(sys.argv[1],"r") as read_file:
    file = read_file.read()
    input_list=[]
    inputs = file.split("\n")
    for input in inputs:
        input2 = input.split("\t") # splitting from \t for handling easier
        input_list.append([input2[0]+input2[1],input2[2]])  # 5 character string for sorting together

input_list.sort() # sorting the input list

a = 1
for t,line in enumerate(input_list):
    if input_list[t-1][0][:4] != line[0][:4]:
        print(f"Message\t{a}",file=output_file) # for printing message and its number
        a+=1  # increasing the message number
        print("{}\t{}\t{}".format(line[0][:4],line[0][4],line[1]),file=output_file)
    else:
        print("{}\t{}\t{}".format(line[0][:4],line[0][4],line[1]),file=output_file)

output_file.close()

# Ahmet Şeref Eker
# Hacettepe Üniversitesi Bilgisayar Mühendisliği
# 2210356098