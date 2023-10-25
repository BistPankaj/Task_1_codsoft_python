print("------------Hey User! I am your calculator------------")
print("Choice Operator +:\t\tFor Addition")
print("Choice Operator -:\t\tFor Subtraction ")
print("Choice Operator *:\t\tFor Multiplication")
print("Choice Operator /:\t\tFor Division ")
while(True):
    try:
        num1=float(input("Please Enter the first number: "))
        num2=float(input("Please Enter the second number: "))
        opr=input("Enter the operator which you want  :-->  +, -, *, / ")
        if opr =='+':
            add=num1+num2
            print("Addition of ",num1,"and ",num2," is: ",add)
        elif opr=='-':
            sub=num1-num2
            print("Subtraction of ",num1,"and ",num2," is: ",sub)
        elif opr=='*':
            multi=num1*num2
            print("Multiplication of ",num1,"and ",num2," is: ",multi)
        elif opr=='/':
            div=num1/num2
            print("Division of ",num1,"and ",num2," is: ",div)
        else :
            print("You Entered wrong Operator!")
            print("Please Entered the correct Operator")
    except :
        print("You Entered wrong input ! ")
            

