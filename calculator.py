import math
import list
import sys

"""
Inputs:
equations -> the current equation we have
i -> the operator, we check the equation for this operator so we know what we're on
occ -> the number of times this operator has been used. If occ > 1, we skip (occ-1) operators
currentNum -> the current answer which is used to help with operations
firstTime -> whether its the first time-- used to ensure we know when to not use current answer
"""
def add(equations:str, i:str, occ=1, currentNum=0, firstTime=False, inParentheses=False) -> float:
    try:
        newEquations = equations
        curInd = 0 # the index of cutoff. Allows us to keep track of where each operator is

        for g in range(occ):
            indexOfI = newEquations.index(i) + curInd # Get the next index of the operator
            newEquations=equations[indexOfI+1::] # The remaining equation after the operator
            curInd = indexOfI + 1 # the starting index of the new equation
        
        # First time
        if currentNum == 0 and firstTime == True:
            firstNum = float(equations[:indexOfI]) 
            secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)]) 
            answer =   firstNum +  secondNum 
        else:
            firstNum = currentNum
            secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
            answer = firstNum +  secondNum

 
        if list.nonNumericIndexBegin(equations, indexOfI) >= len(equations):
            return [answer,0,list.nonNumericIndexEnd(equations, indexOfI+1)]
        return [answer,list.nonNumericIndexBegin(equations, indexOfI)+1,list.nonNumericIndexEnd(equations, indexOfI+1)]
    except Exception as e:
        print(f"Invalid Input: Adding Error: {e}\n")
        sys.exit()

"""
Inputs:
equations -> the current equation we have
i -> the operator, we check the equation for this operator so we know what we're on
occ -> the number of times this operator has been used. If occ > 1, we skip (occ-1) operators
currentNum -> the current answer which is used to help with operations
firstTime -> whether its the first time-- used to ensure we know when to not use current answer
"""
def subtract(equations:str, i:str, occ=1, currentNum=0, firstTime=False) -> float:
    try:
        newEquations = equations
        curInd = 0

        for g in range(occ):
            indexOfI = newEquations.index(i) + curInd # Get the next index of the operator
            newEquations=equations[indexOfI+1::] # The remaining equation after the operator
            curInd = indexOfI + 1 # the starting index of the new equation
        
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

        if list.nonNumericIndexBegin(equations, indexOfI) >= len(equations):
            return [answer,0,list.nonNumericIndexEnd(equations, indexOfI+1)]
        return [answer,list.nonNumericIndexBegin(equations, indexOfI)+1,list.nonNumericIndexEnd(equations, indexOfI+1)]
    except Exception as e:
        print(f"Invalid Subtract Input: Error: {e}\n")
        sys.exit()

"""
Inputs:
equations -> the current equation we have
i -> the operator, we check the equation for this operator so we know what we're on
occ -> the number of times this operator has been used. If occ > 1, we skip (occ-1) operators
currentNum -> the current answer which is used to help with operations
firstTime -> whether its the first time-- used to ensure we know when to not use current answer
"""
def multiply(equations:str, i:str, occ=1, currentNum=0, firstTime=False) -> list:
    try:
        newEquations = equations
        curInd = 0

        indexOfI = newEquations.index(i) + curInd # Get the next index of the operator
        newEquations=equations[indexOfI+1::] # The remaining equation after the operator
        curInd = indexOfI + 1 # the starting index of the new equation
        try:
            firstNum = float(equations[list.nonNumericIndexBegin(equations, indexOfI)+1:indexOfI])
        except:
            firstNum = float(equations[:indexOfI])
        secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
        answer = firstNum * secondNum

        if list.nonNumericIndexBegin(equations, indexOfI) >= len(equations):
            return [answer,0,list.nonNumericIndexEnd(equations, indexOfI+1)]
        return [answer,list.nonNumericIndexBegin(equations, indexOfI)+1,list.nonNumericIndexEnd(equations, indexOfI+1)]
    except Exception as e:
        print(f"Invalid Multiplying Input: Error: {e}\n")
        sys.exit()

"""
Inputs:
equations -> the current equation we have
i -> the operator, we check the equation for this operator so we know what we're on
occ -> the number of times this operator has been used. If occ > 1, we skip (occ-1) operators
currentNum -> the current answer which is used to help with operations
firstTime -> whether its the first time-- used to ensure we know when to not use current answer
"""
def divide(equations:str, i:str, occ=1, currentNum=0, firstTime=False) -> list:
    try:
        newEquations = equations
        curInd = 0

        indexOfI = newEquations.index(i) + curInd # Get the next index of the operator
        newEquations=equations[indexOfI+1::] # The remaining equation after the operator
        curInd = indexOfI + 1 # the starting index of the new equation
        
        try:
            firstNum = float(equations[list.nonNumericIndexBegin(equations, indexOfI)+1:indexOfI])
        except:
            firstNum = float(equations[:indexOfI])
        secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
        answer = firstNum / secondNum

        if list.nonNumericIndexBegin(equations, indexOfI) >= len(equations):
            return [answer,0,list.nonNumericIndexEnd(equations, indexOfI+1)]
        return [answer,list.nonNumericIndexBegin(equations, indexOfI)+1,list.nonNumericIndexEnd(equations, indexOfI+1)]
    except ZeroDivisionError:
        print(f"Invalid Input: Error: cannot divide by zero\n")
        sys.exit()
    except Exception as e:
        print(f"Invalid Input: Dividing Error: {e}\n")
        sys.exit()

"""
Inputs:
equations -> the current equation we have
i -> the operator, we check the equation for this operator so we know what we're on
occ -> the number of times this operator has been used. If occ > 1, we skip (occ-1) operators
currentNum -> the current answer which is used to help with operations
firstTime -> whether its the first time-- used to ensure we know when to not use current answer
"""
def exponent(equations:str, i:str, occ=1, currentNum=0, firstTime=False) -> list:
    try:
        newEquations = equations
        curInd = 0

        indexOfI = newEquations.index(i) + curInd # Get the next index of the operator
        newEquations=equations[indexOfI+1::] # The remaining equation after the operator
        curInd = indexOfI + 1 # the starting index of the new equation
        try:
            firstNum = float(equations[list.nonNumericIndexBegin(equations, indexOfI)+1:indexOfI])
        except:
            firstNum = float(equations[:indexOfI])
        secondNum = float(equations[indexOfI+1:list.nonNumericIndexEnd(equations, indexOfI+1)])
        answer = firstNum ** secondNum

        if list.nonNumericIndexBegin(equations, indexOfI) >= len(equations):
            return [answer,0,list.nonNumericIndexEnd(equations, indexOfI+1)]
        return [answer,list.nonNumericIndexBegin(equations, indexOfI)+1,list.nonNumericIndexEnd(equations, indexOfI+1)]
    except Exception as e:
        print(f"Invalid Multiplying Input: Error: {e}\n")
        sys.exit()


