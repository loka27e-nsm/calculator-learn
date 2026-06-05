import math
import calculator
import sys

"""
Inputs:
    operatorList -> list of remaining operators in equation
    lvlList -> list of operators to watch out for
Output:
    true/false -> whether we have an operator that remains that takes precedence over current operator 
"""
def test(operatorList:list, lvlList:list):
    for index in range(len(operatorList)):
        if operatorList[index] in lvlList:
            return False
    return True

equation = "".join(sys.argv[1:])

# help navigate
if equation == "help":
    print("Functions:\n1. Add (1+1)\n2. Subtract (2-1)\n3. Multiply (4*3)\n4. Divide (4/2)\nEquations evaluated on a PEMDAS basis")
    sys.exit()

# Makes it easier to read
equation = equation.replace(" ","")
if str(equation[0]).isnumeric() == False:
    equation = "0"+equation # ensures adding a symbol at the front doesn't mess it up like a negative number

operation_list = []
firstTime = True
justMultDiv = False
answer = 0
# How ever many times we've done each operator
addCtr = 0 
subCtr = 0
multCtr = 0
divCtr = 0
expCtr = 0

# Get list of operators
for x in range(len(equation)):
    try:
        if equation[x] != "." or equation[x] != "-x":
            n=float(equation[x])
    except:
        # Ensure decimal points not counted as operator
        if equation [x] != ".":
            operation_list.append(equation[x])
#print(f"{operation_list}\n")
newOperatorList = operation_list.copy() # previous: operation_list + []

# List of operators by precendence
firstLvl = ["(",")"]
secondLvl = firstLvl + ["^"]
thirdLvl = secondLvl + ["*","/"]
fourthLvl = thirdLvl + ["+","-"]

while len(newOperatorList) > 0:
    operation_list = list(newOperatorList)
    for i in operation_list:
        # Addition
        if i == "+" and test(newOperatorList,thirdLvl) == True:
            addCtr += 1
            currentAnswer = calculator.add(equation, i, addCtr, answer, firstTime)
            firstTime = False # let the function know we've already done a calculation
            justMultDiv = False
            newOperatorList.remove(i)
            answer = currentAnswer
        # Subtraction
        elif i == "-"and test(newOperatorList,thirdLvl) == True:
            if "-" not in equation:
                while "-" in newOperatorList:
                    newOperatorList.remove("-")
                while "-" in operation_list:
                    operation_list.remove("-")
                continue

            subCtr += 1
            currentAnswer = calculator.subtract(equation, i, subCtr, answer, firstTime)
            firstTime = False
            justMultDiv = False
            newOperatorList.remove(i)
            answer = currentAnswer
        # Multiplication
        elif i == "*"and test(newOperatorList,secondLvl) == True:
            if ("*" in equation) == False:
                while "*" in newOperatorList:
                    newOperatorList.remove("*")
                continue
            multCtr += 1
            currentAnswer = calculator.multiply(equation, i, multCtr, answer, firstTime)
            justMultDiv = True
            try:
                replaceString = equation[currentAnswer[1]:currentAnswer[2]]
                equation = equation.replace(str(replaceString),str(currentAnswer[0]))
            except:
                try:
                    replaceString = equation[currentAnswer[1]:currentAnswer[2]]
                    equation = equation.replace(str(replaceString),str(currentAnswer[0]))
                except:
                    firstTime = False
                    answer = float(currentAnswer[0])
            newOperatorList.remove(i)

        # Division
        elif i == "/"and test(newOperatorList,secondLvl) == True:
            if ("/" in equation) == False:
                while "/" in newOperatorList:
                    newOperatorList.remove("/")
                continue
            divCtr += 1
            currentAnswer = calculator.divide(equation, i, divCtr, answer, firstTime)
            justMultDiv = True
            try:
                replaceString = equation[currentAnswer[1]:currentAnswer[2]]
                equation = equation.replace(str(replaceString),str(currentAnswer[0]))
            except:
                try:
                    replaceString = equation[currentAnswer[1]:currentAnswer[2]]
                    equation = equation.replace(str(replaceString),str(currentAnswer[0]))
                except:
                    firstTime = False
                    answer = float(currentAnswer[0])
            newOperatorList.remove(i)

        # Exponent
        elif i == "^"and test(newOperatorList,firstLvl) == True:
            if ("^" in equation) == False:
                while "^" in newOperatorList:
                    newOperatorList.remove("^")
                continue
            expCtr += 1
            currentAnswer = calculator.exponent(equation, i, expCtr, answer, firstTime)
            justMultDiv = True
            try:
                replaceString = equation[currentAnswer[1]:currentAnswer[2]]
                equation = equation.replace(str(replaceString),str(currentAnswer[0]))
            except:
                try:
                    replaceString = equation[currentAnswer[1]:currentAnswer[2]]
                    equation = equation.replace(str(replaceString),str(currentAnswer[0]))
                except:
                    firstTime = False
                    answer = float(currentAnswer[0])
            newOperatorList.remove(i)

try:
    # It's integer if float equals integer
    try:
        equation = float(equation)
        if int(equation) == float(equation):
            print(f"{int(equation):,}")
            sys.exit()
        else:
            print(f"{equation:,.2f}")
            sys.exit()
    except ValueError:
        pass
    if int(answer) == float(answer):
        answer = int(answer)
        print(f"{answer:,}")
    else:
        print(f"{answer:,.2f}")
except ValueError:
    print(f"{answer:,.2f}")



