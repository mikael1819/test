from os import system
system("cls")

opc=0
while True:
    print("1-restar")
    print("2-sumar")
    print("3-dividir")
    print("4-multiplicar")
    print("5-salir")
    opc=int(input("ingrese una operacion "))
    if opc==1:
        num1=int(input("por favor ingrese un numero "))
        num2=int(input("por favor ingrese un segundo numero "))
        print(num1-num2)
        input("enter para volver al menu ")
        system("cls")
    if opc==2:
        num1=int(input("por favor ingrese un numero "))
        num2=int(input("por favor ingrese un segundo numero "))
        print(num1+num2)
        input("enter para volver al menu ")
        system("cls")
    if opc==3:
        num1=int(input("por favor ingrese un numero "))
        num2=int(input("por favor ingrese un segundo numero "))
        print(num1/num2)
        input("enter para volver al menu ")
        system("cls")
    if opc==4:
        num1=int(input("por favor ingrese un numero "))
        num2=int(input("por favor ingrese un segundo numero "))
        print(num1*num2)
        input("enter para volver al menu ")
        system("cls")
    if opc==5:
        break