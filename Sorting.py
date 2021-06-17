def isCorrect(x):
    while not x.isdigit() :
        if x[0] == "-":
            if x[1:].isdigit():
                return int(x)
            elif "." in x:
                if x[x.index(".") +1: : ].isdigit() and x[1 : x.index(".") : ].isdigit():
                    return float(x) 
                else:
                    x = input("Incorret input, please enter a integer: ")
            else:
                x = input("Incorret input, please enter a integer: ")
        elif "." in x:
            if x[x.index(".") +1: : ].isdigit() and x[0 : x.index(".") : ].isdigit():                    
                return float(x)
            else:
                 x = input("Incorret input, please enter a integer: ")
        else:
            x = input("Incorret input, please enter a integer: ")
    return int(x)

x = input("Please enter the first number: ")
x = isCorrect(x)

y = input("Please enter the second number: ")
y = isCorrect(y)

z = input("Please enter the third number: ")
z = isCorrect(z)

#Uzun
n1 = max(x,y,z)
n2 = min(x,y,z)
n3 = x+y+z - n1 - n2
print("The numbers sorted in descending order: ",n1, n3, n2)

#En kısa
print("The numbers sorted in descending order as a list: ", sorted([x,y,z])[::-1])
