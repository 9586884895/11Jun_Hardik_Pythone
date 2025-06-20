a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a!=0 and b!=0: #true condition
    if a>b:
        print(" A is maximum and value is:",a*b)
    else:
        print(" A is Mininum and value is:",a-b)
else:
    print("Either A or B is zero, please enter non-zero values")