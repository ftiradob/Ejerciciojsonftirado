import json

def listar(doc):
    listacolegios=[]
    for i in doc["@graph"]:
        listacolegios.append(i["title"])
    return listacolegios

def contar(doc):
    cuenta=[]
    acce=input("Introduzca accesibilidad(0 ó 1): ")
    for i in doc["@graph"]:
            if i["organization"]["accesibility"]==acce:
                cuenta.append(i["organization"]["organization-desc"])
    print("Hay",len(cuenta),"colegios con accesibilidad %s" %(acce))

def mostrarid(doc):
    listaid=[]
    cole=input("Introduzca un colegio público: ")
    for i in doc["@graph"]:
        if i["title"]==cole:
            listaid.append(i["id"])
    return listaid

def codigopostal(doc):
    listacoles=[]
    cp=input("Introduzca un codigo postal de Madrid: ")
    for i in doc["@graph"]:
        if i["address"]["postal-code"]==cp:
            listacoles.append(i["title"])
    return listacoles

def ejer5(doc):
    listaaccecp=[]
    accesi=input("Introduzca accesibilidad(0 ó 1): ")
    codi=input("Introduzca un código postal: ")
    for i in doc["@graph"]:
            if i["organization"]["accesibility"]==accesi and i["address"]["postal-code"]<codi:
                listaaccecp.append(i["title"])
    return listaaccecp

with open("colegiospubjson.json") as colegios:
    doc=json.load(colegios)

print("")
while True:
    print("1. Mostrar los nombres de todos los colegios públicos.")
    print("2. Mostrar la cantidad de colegios públicos los cuales tengan una accesibilidad pedida por teclado.")
    print("3. Pedir un colegio por teclado y mostrar su id.")
    print("4. Pedir un codigo postal por teclado y mostrar el/los colegios que pertenecen al mismo.")
    print("5. Mostrar todos los colegios que tengan una accesibilidad pedida por teclado y un codigo postal menor que el pedido por teclado.")
    print("0. Salir")
    opcion=int(input("Elija opción: "))

    if opcion==1:
        print("")
        for i in listar(doc):
            print("-",i)
        print("")
    elif opcion==2:
        contar(doc)
    elif opcion==3:
        for i in mostrarid(doc):
            print("->",i)
        print("")
    elif opcion==4:
        for i in codigopostal(doc):
            print("-",i)
        print("")
    elif opcion==5:
        for i in ejer5(doc):
            print("-",i)
        print("")
    elif opcion==0:
        print("Adios")
        break
    else:
        print("Error de opción")