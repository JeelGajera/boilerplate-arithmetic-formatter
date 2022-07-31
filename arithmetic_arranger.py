import re
def arithmetic_arranger(problems, call = False):
    if (len(problems) > 5):
        return "Error: Too many problems."
    firs_line =  ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    for problem in problems:
        if (re.search("[^\s0-9.+-]", problem)):
            if (re.search("['/']", problem) or re.search("['*']", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        firs_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_number = problem.split(" ")[2]
        if (len(firs_number) > 4 or len(second_number) > 4):
            return "Error: Numbers cannot be more than four digits."
        sum = ""
        if (operator == "+"):
            sum = str(int(firs_number) + int(second_number))
        elif (operator == "-"):
            sum = str(int(firs_number) - int(second_number))
        length = max(len(firs_number), len(second_number)) + 2
        num1 = str(firs_number).rjust(length)
        num2 = operator + str(second_number).rjust(length-1)
        line = ""
        for i in range(length):
            line += "-"
        res = str(sum).rjust(length)
        if problem != problems[-1]:
            firs_line += num1 + "    " 
            second_line += num2 + "    "
            third_line += line + "    "
            fourth_line += res + "    "
        else:
            firs_line += num1
            second_line += num2 
            third_line += line
            fourth_line += res 
    if call:
        string = firs_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line
    else:
        string = firs_line + "\n" + second_line + "\n" + third_line
    return string