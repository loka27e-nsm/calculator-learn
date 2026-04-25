import math
import calculator
import sys

equation = "".join(sys.argv[1:])

# Makes it easier to read
equation = equation.replace(" ","")
if str(equation[0]).isnumeric() == False:
    equation = "0"+equation

operation_list = []
answer = 0
addCtr = 0
subCtr = 0
multCtr = 0
divCtr = 0

# Get list of operators
for x in range(len(equation)):
    try:
        if equation[x] != "." or equation[x] != "-x":
            n=float(equation[x])
    except:
        operation_list.append(equation[x])

for i in operation_list:
    if i == "+":
        addCtr += 1
        currentAnswer = calculator.add(equation, i, addCtr, answer)
        answer = currentAnswer
    if i == "-":
        subCtr += 1
        currentAnswer = calculator.subtract(equation, i, subCtr, answer)
        answer = currentAnswer
    if i == "*":
        multCtr += 1
        currentAnswer = calculator.multiply(equation, i, multCtr, answer)
        answer = currentAnswer
    if i == "/":
        divCtr += 1
        currentAnswer = calculator.divide(equation, i, divCtr, answer)
        answer = currentAnswer

try:
    if int(answer) == float(answer):
        answer = int(answer)
        print(f"{answer:,}")
    else:
        print(f"{answer:,.2f}")
except:
    print(f"{answer:,.2f}")
    
"""
WHEN GET BACK
    FIX SUBTRACTION. 6*-2 SHOULD WORK
"""



