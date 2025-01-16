from os import system
system("cls")

contra3=""
contra2=""
contra=""
user=""
user2=""
user3=""
while True:
    print("1.registro")
    print("2.iniciar sesion")
    print("3.salir")
    
    opc=int(input("ingrese una opcion: "))
    if opc==1:
        print("cree el usuario que quiera user1, user2, user3")
        op=int(input("ingrese una opcion: "))
        match op:
            case 1:
                user=input("crea un nombre de usuario: ")
                contra=input("ahora crea la cotraseña: ")
            case 2:
                user2=input("crea un nombre de usuario 2: ")
                contra2=input("ahora crea la cotraseña 2: ")
            case 3:
                user3=input("crea un nombre de usuario 3: ")
                contra3=input("ahora crea la cotraseña 3: ")
        if len(user)>=3 and len(user)<=10 and len(user2) >=3 and len(user2)<=10 and len(user3) >=3 and len(user3)<=10:
            print("usuario creado con exito")
        else:
            print("no cumple con el minimo de 3 caracteres o el maximo de 10 caracteres")
            input("press enter para volver al menu principal")
            system("cls")
        if len(contra)>=4 and len(contra)<=10 and len(contra2)>=4 and len(contra2)<=10 and len(contra3) >=4 and len(contra3)<=10:
         print("no cumple con el minimo de 3 caracteres o el maximo de 10 caracteres")
         input("press enter para volver al menu principal")
         system("cls")
    if opc==2:
        if user=="" and user2=="" and user3=="":
            print("no hay usuarios registrados")
        else:
            print(user,user2,user3)
            print("inicio sesion")
            nombre=input("por favor ingrese su nombre de usuario: ")
            contraseña=input("por favor ingrese su contraseña: ")
        if contraseña==contra and nombre==user:
            print("bienvenido",user)
            input("press enter para volver al menu principal")
            system("cls")
        if contraseña==contra2 and nombre==user2:
            print("bienvenido",user2)
            input("press enter para volver al menu principal")
            system("cls")
        if contraseña==contra3 and nombre==user3:
            print("bienvenido",user2)
            input("press enter para volver al menu principal")
            system("cls")
        else:
            print("no es usted")
            input("press enter para volver al menu principal")
            system("cls")
    if opc==3:
        system("cls")
        print("vuelva pronto")
        break