# This python file is a module, which contains basic arithmatic functions

def Add(Num1, Num2):
    Result = Num1 + Num2
    print(f"Addition of {Num1} & {Num2} : {Result}")

def Sub(Num1, Num2):
    if Num1 >= Num2:
        Result = Num1 - Num2
        print(f"Substraction of {Num1} & {Num2} : {Result}")
    else:
        Result = Num2 - Num1
        print(f"Substraction of {Num2} & {Num1} : {Result}")

def Mult(Num1, Num2):
    Result = Num1 * Num2
    print(f"Multiplication of {Num1} & {Num2} : {Result}")

def Div(Num1, Num2):
    if Num1 >= Num2 and Num2 != 0:
        Result = Num1 / Num2
        print(f"Division of {Num1} & {Num2} : {Result}")
    elif Num2 > Num1 and Num1 != 0:
        Result = Num2 / Num1
        print(f"Division of {Num2} & {Num1} : {Result}")
    else:
        print("Denominator can not Zero")
