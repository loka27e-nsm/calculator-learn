import math
import list
import sys

"""
Inputs:
equations -> the current equation we have
i -> the operator, we check the equation for this operator so we know what we're on
occ -> the number of times this operator has been used. If occ > 1, we skip (occ-1) operators
currentNum -> the current answer
"""
def add(equations, i, occ=1, currentNum=0, firstTime=False) -> float:
    try:
        newEquations = equations
        curInd = 0

        for g in range(occ):
            indexOfI = newEquations.index(i) + curInd
            newEquations=equations[indexOfI+1::]
            curInd = indexOfI + 1
        
        if currentNum == 0 and firstTime == True:
            firstNum = float(equations[:indexOfI])
            secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
            answer =   firstNum +  secondNum 
        else:
            firstNum = currentNum
            secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
            answer = firstNum +  secondNum

        return answer
    except Exception as e:
        print(f"Invalid Input: Adding Error: {e}\n")
        sys.exit()

def subtract(equations, i, occ=1, currentNum=0, firstTime=False) -> float:
    try:
        newEquations = equations
        curInd = 0

        for g in range(occ):
            indexOfI = newEquations.index(i) + curInd
            newEquations=equations[indexOfI+1::]
            curInd = indexOfI + 1
        
        try:
            n = float(equations[indexOfI-1])
        except:
            return currentNum

        if currentNum == 0 and firstTime == True:
            firstNum = float(equations[:indexOfI])
            secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
            answer =   firstNum -  secondNum 
        else:
            firstNum = currentNum
            secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
            answer = firstNum -  secondNum

        return answer
    except Exception as e:
        print(f"Invalid Subtract Input: Error: {e}\n")
        sys.exit()

def multiply(equations, i, occ=1, currentNum=0, firstTime=False) -> float:
    try:
        newEquations = equations
        curInd = 0

        for g in range(occ):
            indexOfI = newEquations.index(i) + curInd
            newEquations=equations[indexOfI+1::]
            curInd = indexOfI + 1
        
        if currentNum == 0 and firstTime == True:
            firstNum = float(equations[:indexOfI])
            secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
            answer = firstNum * secondNum
        else:
            firstNum = currentNum
            secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
            answer = firstNum *  secondNum

        return answer
    except Exception as e:
        print(f"Invalid Multiplying Input: Error: {e}\n")
        sys.exit()

def divide(equations, i, occ=1, currentNum=0, firstTime=False) -> float:
    try:
        newEquations = equations
        curInd = 0

        for g in range(occ):
            indexOfI = newEquations.index(i) + curInd
            newEquations=equations[indexOfI+1::]
            curInd = indexOfI + 1
        
        if currentNum == 0 and firstTime == True:
            firstNum = float(equations[:indexOfI])
            secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
            answer =   firstNum /  secondNum 
        else:
            firstNum = currentNum
            secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
            answer = firstNum /  secondNum

        return answer
    except ZeroDivisionError:
        print(f"Invalid Input: Error: cannot divide by zero\n")
        sys.exit()
    except Exception as e:
        print(f"Invalid Input: Dividing Error: {e}\n")
        sys.exit()

