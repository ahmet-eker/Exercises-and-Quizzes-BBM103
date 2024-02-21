# coding: utf8

import sys

def round_up(number):  # round function
    return int(number)+1

try:
    the_input_file = sys.argv[1]  # input file
    the_comparison_file = sys.argv[2] # comparison file
    with open(the_input_file,"r",encoding = "utf-8") as file:
        read_input = file.read()
        inputs = read_input.split("\n")
    with open(the_comparison_file,"r",encoding = "utf-8") as file2:
        read_comparison_input = file2.read()
        comparison_input = read_comparison_input.split("\n")
except IndexError: # handling the file errors before main code
    print("IndexError: number of input files less than expected.")
except IOError:
    print("IOError: cannot open {}".format(the_comparison_file))
else:  # if there are no errors
    for i,input in enumerate(inputs):
        print("------------")
        try:
            inputs_list = input.split(" ")  # splitting from space
            if (float(inputs_list[0])-int(float(inputs_list[0])))<0.5:  #rounding the div and nondiv number
                div = int(float(inputs_list[0]))
            else:
                div = round_up(inputs_list[0])
            if float(inputs_list[1])-int(float(inputs_list[1]))<0.5:
                nondiv = int(float(inputs_list[1]))
            else:
                nondiv = round_up(inputs_list[1])
            from_ = float(inputs_list[2])
            to = float(inputs_list[3])
            result_list = []  # creating a result list
            for number in range(round_up(from_),int(to)+1):
                if number % div == 0 and number % nondiv != 0:
                    result_list.append(number)
            result_string = ""
            for member in result_list: # turning list to a string for visualization
                result_string = result_string + " " + str(member)
            comparison_string = ""
            for member in [int(i) for i in comparison_input[i].split(" ")]:
                comparison_string = comparison_string + " " + str(member)

            print("My result:               {}".format(result_string))
            print("Result to compare:       {}".format(comparison_string))
            if result_list != [int(i) for i in comparison_input[i].split(" ")]:
                raise AssertionError
        except IndexError:
            print("IndexError: number of operands less than expected.")
            print("Given Input:              {}".format(input))
        except ValueError:
            print("ValueError: only numeric input is accepted.")
            print("Given Input:              {}".format(input))
        except ZeroDivisionError:
            print("ZeroDivisionError: You can't divide by 0.")
            print("Given Input:              {}".format(input))
        except AssertionError:
            print("Assertion Error: results don't match.")
        except Exception:
            print("Given Input:              {}".format(input))
            print("kaBOOM: run for your life!.")
        else:
            print("Goool!!!")
finally:
    print("\n- Game Over -")

# Ahmet Seref Eker
# 2210356098
# Hacettepe University Computer Engineering