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
def miltiplicasion():
        num1=int(input("por favor ingrese un numero "))
        num2=int(input("por favor ingrese un segundo numero "))
        print(num1*num2)
def par_inpar():
        num=8
        if num%2==0:
            print("el numero es par")
        else:
            print("el numero es impar")
def ver_par_inpar():
        num=8
        if num%2==0 and num>0 :
            print("el numero es par")
        else:
            print("el numero es impar")
