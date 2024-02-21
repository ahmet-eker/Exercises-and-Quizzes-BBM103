import sys

file = open(sys.argv[1],"r")
read_file= file.read()
students = read_file.split("\n")
student_dict = {}
for student in students:
    student_dict[student.split(":")[0]] = student.split(":")[1]

wanted_students = sys.argv[2].split(",")
for student in wanted_students:
    try:    
        print("Name: {}, University: {}".format(student,student_dict[student]))
    except KeyError:
        print("No record of {} was found!".format(student))