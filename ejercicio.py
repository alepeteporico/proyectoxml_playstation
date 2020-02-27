from lxml import etree
datos=etree.parse("Playstation.xml")
from funciones import * 

while True:
    print("=============================================MENÚ=============================================")
    print("1. Listar consolas de sobremesa o portatiles y después te pregunta si quieres listar los juegos de alguna de ellas.")
    print("2. Contar los juegos de una consola en total y también los que son exclusivos.")
    print("3. Introduce una fecha y te muestra todas las consolas que salieron antes de esa fecha.")
    print("4. Introducir por teclado un juego y te dice de que consola es y el precio de la consola de salida.")
    print("5. Un juego donde eliges una consola y te dice todos los juegos que salieron en ella y tienes 3 intentos para acertar cual fue el mas vendido de la misma.")
    print("6. Salir")
    print("==============================================================================================")
    opc=int(input("Elige una opción: "))
    print("")

    if opc==1:
        print("----SOBREMESA----")
        for consola in ej1(datos)[0]:
            print("-",consola)
        
        print("----PORTATIL----")
        for consola in ej1(datos)[1]:
            print("-",consola)
        
        opcion=input("¿Quieres listar los juegos de alguna consola? (s/n): ")

        while opcion=="s":
            consola=input("Dime la consola de la que quieres listar los juegos: ")
            for juego in ej1_2(datos,consola):
                print("-",juego)
            print("--------------------")
            opcion=input("¿Quieres listar los juegos de alguna consola? (s/n): ")
        print("------------------------------------------------------------------")
        print("")

    elif opc==2:
        consola=input("Dime la consola de la que quieres contar los juegos: ")
        print("El numero de juegos de la",consola,"Es",ej2(datos,consola)[0])
        print("El numero de exclusivos de la",consola,"Es",ej2(datos,consola)[1])
        print("------------------------------------------------------------------")
        print("")

    elif opc==3:
        fecha=input("Dime un año: ")
        for consola in ej3(datos,fecha):
            print("-",consola)
        print("------------------------------------------------------------------")
        print("")

    elif opc==4:
        juego=input("Dime un juego: ")
        print("Salio en",ej4(datos,juego)[0],"El precio de esta consola de salida fue",ej4(datos,juego)[1])
        print("------------------------------------------------------------------")
        print("")
        

    elif opc==6:
        break

    else:
        print("ERROR, ESTÁ OPCIÓN NO EXISTE.")