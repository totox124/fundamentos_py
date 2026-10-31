"""Se realizara un script en el que se agregaran 3 elementos a elementos.txt mediante input y luego lo recorra e imprima en pantalla tal que 1. elemento 1

"""


while True:
    try:
        opc = int(input(" agregar(1).\n sobreescribir(2).\n leer(3).\n salir(4).\n elija una (solo se permite agregar 3 elementos): "))
    except ValueError:
        print("solo numeros enteros")
        continue
    if opc == 1:
        contador = 0
        while contador <= 3:
            with open("elementos.txt", "a", encoding="utf-8") as archivo:
                texto = input("agregue un elemento")
                archivo.write(texto + "\n")
                contador += 1
        continue
    elif opc == 2:
        
                with open("elementos.txt", "w", encoding="utf-8") as archivo:
                    texto = input("agregue un elemento")
                    archivo.write(texto + "\n")
                    

    elif opc == 3: 
        with open("elementos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                print(linea.strip())

    elif opc == 4:
        break

    else:
        print("opcion invalida, intente nuevamente")
        continue