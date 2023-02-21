def arithmetic_arranger(string, option = False):
    if len(string) >5:
        return "Error: Too many problems."
    mostDigitAmount = []
    firstNumberList = []
    secondNumberList = []
    operandList = []
    resultList = []
    for entry in string:
        values = (entry.split(" "))
        try:
            int(values[0])
            int(values[2])
        except:
            return "Error: Numbers must only contain digits."
        firstNumberList.append(int(values[0]))
        secondNumberList.append(int(values[2]))
        operandList.append(values[1])
        resultList.append(obtain_result(values))
        mostDigitAmount.append(obtain_digitAmount(max(int(values[0]), int(values[2]))))
        
        if values[1] != "+":
            if values[1] != "-":
                return "Error: Operator must be '+' or '-'."
        if int(len(values[0]))> 4 or int(len(values[2])>4):
            return "Error: Numbers cannot be more than four digits."
    line1 = make_line1(mostDigitAmount, firstNumberList)
    line2 = make_line2(mostDigitAmount, secondNumberList, operandList)
    line3 = make_line3(mostDigitAmount)
    line4 = make_line4(mostDigitAmount, resultList)
    
    if option == True:
        return line1+line2+line3+line4
    else:
        return line1+line2+line3


def make_line4(mostDigit, resultList):
    line4 = "\n"
    for item in range(len(mostDigit)):
        line = " " * (2 + mostDigit[item] - obtain_digitAmount(resultList[item])) + str(resultList[item])
        if item == 0:
            line4 += line
        else:
            line4 += " "*4 +line
    return line4

def make_line3(mostDigit):
    line3 ="\n"
    for item in range(len(mostDigit)):
        line = "-" * (mostDigit[item] + 2)
        if item == 0:
            line3 += line
        else:
            line3 += " "*4+line
    return line3

def make_line2(mostDigit, secondNumber, operator):
    line2 = "\n"
    for item in range(len(mostDigit)):
        line = operator[item] + " " * (1 + mostDigit[item] - obtain_digitAmount(secondNumber[item])) + str(secondNumber[item])
        if item == 0:
            line2 += line
        else:
            line2 += " "*4 + str(line)
    return line2

def make_line1(mostDigit, firstNumber):
    line1 = ""
    for item in range(len(mostDigit)):
        if item < len(mostDigit):
            line = " " * (2 + mostDigit[item] - obtain_digitAmount(firstNumber[item])) + str(firstNumber[item])
            if item == 0:
                line1 += line
            else:
                line1 +=" "*4 + line
        else:
            break
    return line1

def obtain_result(value):
    result = 0
    if(value[1] == "-"):
        result = int(value[0]) - int(value[2])
    else:
        result = int(value[0]) + int(value[2])
    return result

def obtain_digitAmount(digit):
    digitAmount = 1
    digitTotal = digit
    while digitTotal >= 10 or digitTotal <= -10:
        digitTotal = digitTotal/10
        digitAmount += 1
    if digitTotal < 0:
        digitAmount += 1
    return digitAmount