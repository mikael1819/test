from os import system
system("cls")


# nombre=["pedro","juan","diego"]
# apellido=["lope","gonzales","sepulveda"]
# numero=["primer","segundo","tercero"]
# for i in range(len (nombre)):
#     print(nombre[i],apellido[i])
#     print("el",numero[i],nombre[i])

# fruta=["fruta del dragon","pera","manzana","durian","platano"]
# while True:
#     print("1.ver las frutas")
#     print("2. agregar una fruta")
#     print("3.quitar una fruta")
#     print("4.salir")
#     f=int(input("ingrede un numero: "))
#     match f:
#         case 1:
#             print(fruta)
#             input("press enter para continuar")
#             system("cls")
#         case 2:
#             m=input("agregue una fruta: ")
#             fruta.append(m)
#             print(fruta)
#             input("press enter para continuar")
#             system("cls")
#         case 3:
#             r=input("que fruta quiere quitar: ")
#             fruta.remove(r)
#             print(fruta)
#             input("press enter para continuar")
#             system("cls")
#         case 4:
#             break

total=0
carro=[]
nombre=["pedro","juan","diego"]
fruta=["fruta del dragon $7,990","pera $3000","manzana $7000","durian $4000","platano $5000"]
while True:
    print("1.quien de las perras va a comprar")
    print("2.agregar una fruta")
    print("3.ver la cariñosa")
    print("4.adios perra")
    f=int(input("ingrede una opcion: "))
    match f:
        case 1:
            print("quien va a comprar")
            for i in nombre:
                print(i)
            n=input("ingrese el nombre: ")
            input("press enter para continuar")
            system("cls")
        case 2:
            while True:
                system("cls")
                print("1-fruta del dragon $7,990 \n2-pera $3000 \n3-manzana $7000 \n4-durian $4000 \n5-platano $5000\n6- volver al menu principla pedaso de perra : chupalo")
                m=int(input("agregue una fruta: "))
                match m:
                    case 1:
                        carro.append("fruta del dragon")
                        total=total+7990
                        input("press enter para continuar")
                        system("cls")
                    case 2:
                        carro.append("pera")
                        total=total+3000
                        input("press enter para continuar")
                        system("cls")
                    case 3:
                        carro.append("manzana")
                        total=total+7000
                        input("press enter para continuar")
                        system("cls")
                    case 4:
                        carro.append("durian")
                        total=total+4000
                        input("press enter para continuar")
                        system("cls")
                    case 5:
                        carro.append("platano")
                        total=total+5000
                        input("press enter para continuar")
                        system("cls")
                    case 6:
                        print("volviendo a ser perra")
                        print(carro)
                        input("press enter para continuar")
                        system("cls")
                        break
        case 3:
            print("------ BOLETA------")
            print(f"{n} esta es su boleta")
            print("productos:")
            for f in range(len (carro)):
                print(carro[f])
            print("su total a pagar es ", total)
            break
        case 4:
            print("chao perra besos en el corta churro")
            break
        case _:
            print("ingresa una opcion correcta  OEEEEEE")