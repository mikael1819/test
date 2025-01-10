from os import system
system("cls")

#edad=int(input("por favor ingrese su edad mi hermosa persona: "))
#if edad>10 and edad<=18:
#    print("el valor se su boleto es $1000")
#if edad>18 and edad<=65:
#    print("el valor se su boleto es $2000")
#if edad>65:
#    print("el valor se su boleto es $1500")
#else:
#    print("usted entra gratis")

#segundo ejercicio

#num1=int(input("ingrese un numero por favor: "))
#num2=int(input("ingrese un segundo numero por favor: "))
#if num1<num2:
#    print("el numero mayor es el",num2)
#else:
#    print("el numero mayor es el",num1)

# ejercicio 3

#e=int(input("por favor ingrese un numero: "))
#for i in range(10):
#    i+1
#    tabla=(i+1)*e
#    print(e,"x",i+1,"=",tabla)

#ejercicio 4

total=0
while True:
    print("1-Ingresar Nombre del cliente")
    print("2-Mostrar Menú de Platos junto con sus precios")
    print("3-Mostrar Saludo al cliente")
    print("4-salir")
    opc=int(input("ingrese una opcion: "))
    if opc==1:
        nombre=input("ingrese el nombre por favor: ")
        input("precione enter para continuar")
        system("cls")
    if opc==2:
        print("Arroz a la francesa $4.500")
        print("Arroz marinero $5.200")
        print("Sopa marinera $9.700")
        input("precione enter para continuar")
        system("cls")
    if opc==3:
        print ("el nombre del cliente es ",nombre)
        input("precione enter para continuar")
        system("cls")
    if opc==4:
        print("vuelva pronto")
        break