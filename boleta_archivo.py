from os import system
system("cls")

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
            with open ('boleta','w') as archivo:
             for f in range(len (carro)):
                archivo.write(f"------ BOLETA------\n{n} esta es su boleta\nproductos:\n{carro[f]}\nsu total a pagar es {total}")
                break
        case 4:
            print("chao perra besos en el corta churro")
            break
        case _:
            print("ingresa una opcion correcta  OEEEEEE")