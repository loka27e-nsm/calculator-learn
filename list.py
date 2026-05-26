
"""
ENSURE IF OPERATOR ISNT SUBTRACTION WE TREAT IT AS NEG NUMBER
"""
def nonNumericIndexEnd(list:str,startIndex:int) -> int:
    for x in range(startIndex, len(list)):
        try:
            if list[x] != ".":
                if list[x] == "-" and str(list[x-1]).isnumeric() == False:
                    continue
                n=float(list[x]) # when its not a number, throw error and return this index to determine the end of the equation
        except:
            return x
    return len(list)

"""def nonNumericIndexBegin(list,startIndex) -> int:
    for x in range(startIndex, 0,-1):
        try:
            if list[x] != ".":
                n=float(list[x])
        except:
            return x
    return len(list)"""