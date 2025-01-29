import json
from os import system
system("cls")

d={}
while True:
    try:
        a=input("ingrese nombre: ")
        e=int(input("ingresu su edad: "))
        d[a]=e
        sn=input("quiere ingresar otrosnombres??? s/n: ")
        if sn == "n":
            break
        else:
            continue
    except:
        print("usted ingrese un valor no valido")
for k,v in d.items():
    print("nombre",k,"edad",v)
with open ('mi_archivo.json','w') as archivo:
    json.dump(d,archivo)
#opcion 2
    
# d={}
# sn=0
# while sn!="n":
#     try:
#         a=input("ingrese nombre: ")
#         e=int(input("ingresu su edad: "))
#         d[a]=e
#         sn=input("quiere ingresar otrosnombres??? s/n: ")
#     except:
#         print("usted ingrese un valor no valido")
# for k,v in d.items():
#     print("nombre",k,"edad",v)