# Vamos a hacer un inventario similar al del modulo 03, pero ahora mas ordenado, con sus respectivas funciones y demas

""" Empezamos definiendo que funciones debe tener el inventario, por ejemplo:
el inventario debe contener la funcion de agregar el producto y revisar el inventario mediante un bucle for.
cabe recalcar que todos deben tener su try-except para prevenir excepciones.

"""
inventario = {} #creamos el inventario

def agregar(producto, precio):  # Aqui agregamos productos al diccionario
    
    inventario[producto] = precio
    return inventario

def revisar_inventario():  # Con esto revisamos el invent
    
        if not inventario:  # Aqui nos aseguramos que, si no existe un inventario, no continue
            return ("inventario vacio")
        texto = ""
        
        for producto, precio in inventario.items():
                texto += f"{producto} : ${precio}, "
        return texto
                
while True:
    try:
        opc = int(input("agregar producto(1). revisar el inventario(2). salir(3): "))
    except ValueError:
        print("porfavor, solo numeros enteros")
        continue
    if opc == 1:
        producto = input("nombre del producto que desea agregar: ")
        
        while True:
            try:
                precio = int(input("precio del producto: "))
            except ValueError:
                print("porfavor, solo numeros enteros")
                continue
            break
        add = agregar(producto, precio)
        print(add)
    elif opc == 2:
        print(revisar_inventario())

    elif opc == 3:
         break
    else:
         print("opcion invalida, porfavor, ingrese denuevo")
         continue