# Haremos un inventario interactivo, el usuario ingresa un producto, se agrega a la lista o diccionario y siesque quiere, se imprime toda la lista

inventario = {}
while True: 
    try:
        opc = int(input("desea agregar un producto(1) o salir (2)? "))
        if opc == 1:
            producto = input("nombre del producto: ")
            try:
                precio = int(input("precio del producto: "))
            except ValueError:
                    print("caracter invalido, porfavor, ingrese numeros enteros")
                    continue
            inventario[producto] = precio
            print(inventario)
            try:
                opc = int(input("desea agregar un producto(1), salir(2) o ver el inventario(3)? "))
            except ValueError:
                    print("caracter invalido, porfavor, solo numeros enteros")
                    continue
        if opc == 3:
                   
                for producto, precio in inventario.items():
                    print(f"{producto} : {precio}")
                    
        elif opc == 2:
            break
        elif opc > 3:
            print("opcion invalida")
        
    
    except ValueError:
        print("caracter invalido, porfavor, ingrese numeros enteros")
        continue


