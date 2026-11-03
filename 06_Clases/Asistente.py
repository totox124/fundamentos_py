# Comenzaremos ahora con las clases

class asistente():
    def __init__(self, nombre="edith", memoria=None): # ESTOS SON LOS CIMIENTOS, EL INIT ES QUIEN CREA LOS ATRIBUTOS DE NUESTRA CLASE
        self.nombre = nombre  # AQUI LE ASIGANAMOS EL ATRIBUTO NOMBRE, PORQUE TIENE O TENDRA NOMBRE
        self.memoria = memoria if memoria is not None else [] # ESTO PARA LA MEMORIA, SI NO HAY MEMORIA SIMPLEMENTE HAY UNA LISTA VACIA
        self.activo = True   # ESTE ES PARA EL ESTADO, SI ESTA ACTIVO ES TRUE, SI NO ES FALSE

    def saludar(self):
        print(f"hola, mi nombre es {self.nombre} y estoy para servirle")

    def estado_memoria(self):
        try:
            with open("memoria", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    print(linea + ", ")
        except FileNotFoundError:
                print("La memoria se encuentra vacia. Por favor, agregue datos")

    def agregar_memoria(self):
        with open("memoria", "a", encoding="utf-8") as archivo:
            add_memoria = input("dato nuevo que desea agregar y guardar: ")
            archivo.write(add_memoria + "\n")
            
            
            
        

objeto = asistente()
objeto.saludar()

objeto.estado_memoria()
