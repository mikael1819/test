from os import system
system("cls")

def resta():
        num1=int(input("por favor ingrese un numero "))
        num2=int(input("por favor ingrese un segundo numero "))
        print(num1-num2)
def suma():
        num1=int(input("por favor ingrese un numero "))
        num2=int(input("por favor ingrese un segundo numero "))
        print(num1+num2)
def divicion():
        num1=int(input("por favor ingrese un numero "))
        num2=int(input("por favor ingrese un segundo numero "))
        print(num1/num2)
def multiplicasion():
        num1=int(input("por favor ingrese un numero "))
        num2=int(input("por favor ingrese un segundo numero "))
        print(num1*num2)

while True:
        print("1.sumar")
        print("2.restar")
        print("3.dividir")
        print("4.multiplicar")
        print("5.salir")
        op=int(input("ingrese un numero: "))
        match op:
                case 1:
                        print("suma")
                        suma()
                        input("press enter")
                        system("cls")
                case 2:
                        print("resta")
                        resta()
                        input("press enter")
                        system("cls")
                case 3:
                        print("divicion")
                        divicion()
                        input("press enter")
                        system("cls")
                case 4:
                        print("multiplicacion")
                        multiplicasion()
                        input("press enter")
                        system("cls")
                case 5:
                        print("vuelva pronto")
                        break
                case _:
                        print("error pon un numero de los que se muestra en pantalla")