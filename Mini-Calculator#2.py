A = int(input("num1:"))
B = int(input("num2:"))
operation = input("+,-,/,*:")
if(operation=="+"):
    print(A+B)
elif(operation=="-"):
    print(A-B)
elif(operation=="/"):
    print(A/B)
elif(operation=="*"):
    print(A*B)
else:
    print("Invalid Operator")
