import math
import calculator
import sys

equation = "".join(sys.argv[1:])

# help navigate
if equation == "help":
    print("Functions:\n1. Add (1+1)\n2. Subtract (2-1)\n3. Multiply (4*3)\n4. Divide (4/2)\nEquations evaluated on a left to right basis")
    sys.exit()

# Makes it easier to read
equation = equation.replace(" ","")
if str(equation[0]).isnumeric() == False:
    equation = "0"+equation # ensures adding a symbol at the front doesn't mess it up like a negative number

operation_list = []
firstTime = True
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
        # Ensure decimal points not counted as operator
        if equation [x] != ".":
            operation_list.append(equation[x])
print(f"{operation_list}\n")

for i in operation_list:
    if i == "+":
        addCtr += 1
        currentAnswer = calculator.add(equation, i, addCtr, answer, firstTime)
        firstTime = False
        answer = currentAnswer
    if i == "-":
        subCtr += 1
        currentAnswer = calculator.subtract(equation, i, subCtr, answer, firstTime)
        firstTime = False
        answer = currentAnswer
    if i == "*":
        multCtr += 1
        currentAnswer = calculator.multiply(equation, i, multCtr, answer, firstTime)
        firstTime = False
        answer = currentAnswer
    if i == "/":
        divCtr += 1
        currentAnswer = calculator.divide(equation, i, divCtr, answer, firstTime)
        firstTime = False
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



