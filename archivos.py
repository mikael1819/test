import json
from os import system
system("cls")

lista=["mario","luigui","peach"]
def vari():
    return input()

# with open ('mi_archivo.txt','w') as archivo:
#     archivo.write(vari())
# cont=archivo.read()
# print(cont)
# archivo.close()

# datos={}
# d=input("ingrese nombre: ")
# a=int(input("ingrese una clave: "))
# datos[d]=a
# with open ('mi_archivo.json','w') as archivo:
#     json.dump(datos,archivo)

with open ('archivo.txt','w') as archivo:
    for i in lista:
        archivo.write(f"{i}\n")