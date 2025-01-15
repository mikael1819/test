
from os import system
system("cls")
#ejercicio n°1
num=int(input("ingrese un numero para el conteo atras: "))
for i in range (num):
    print(num-(i+1)+1)
    if num-(i+1)+1==1:
        print("se acabo el tiempo")
input("presione enter para ir al siguiente ejercicio: ")
system("cls")  


#ejercicio n°2


num1=int(input("ingrese un numero: "))
num2=int(input("ingrese un segundo numero: "))
num3=int(input("ingrese un tercer numero: "))
if num1>num2 and num1>num3:
    print("el numero mayor de los 3 es: ",num1)
if num2>num3 and num2>num1:
    print ("el numero mayor de los 3 es: ",num2)
if num3>num2 and num3>num1:
    print("el numero mayor de los 3 es: ", num3)
input("presione enter para ir al siguiente ejercicio: ")
system("cls")
 
 
#ejercicio n°3


num4=int(input("ingrese un numero para realizar la tabla: "))
for i in range(10):
    tabla=num4*(i+1)
    print(num4,"x",i+1,"=",tabla)
input("presione enter para ir al siguiente ejercicio: ")
system("cls")
 
 
#ejercicio n°4


total=0
while True:
    print("1. Ingresar Nombre del cliente")
    print("2. Menú de Platos junto con sus precios")
    print("3. Total Boleta")
    print("4. Salir")
    
    opc=int(input("ingrese una opcion por favor: "))
    
    if opc==1:
        nombre=input("por favor ingrese su nombre: ")
        input("presione enter para continuar")
        system("cls")
    if opc==2:
        system("cls")
        while True:
            print("1. Arroz a la francesa $4.500")
            print("2. Arroz marinero $5.200")
            print("3. Sopa marinera $9.700")
            print("4. volveral menu principal")
            opc2=int(input("por favor ingrese un plato: "))
            if opc2==1:
                print("se agrago Arroz a la francesa a la boleta")
                total=total+4500
                input("presione enter para continuar")
                system("cls")
            if opc2==2:
                print("se agrego Arroz marinero a la boleta")
                total=total+5200
                input("presione enter para continuar")
                system("cls")
            if opc2==3:
                print("se agrego Sopa marinera a la boleta")
                total=total+9700
                input("presione enter para continuar")
                system("cls")
            if opc2==4:
                system("cls")
                break
    if opc==3:
        print(nombre," su total es de ",total)
        input("presione enter para continuar")
        system("cls")
    if opc==4:
        print("vuelva pronto")
        break