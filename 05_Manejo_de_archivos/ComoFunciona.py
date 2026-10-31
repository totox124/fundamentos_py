# Ahora, comenzaremos con el manejo de archivos
# encoding=utf-8 sirve para que el interprete detecte todo simbolo sin tirar error con tildes o letras que no hay en ingles.
# With actua como gestor, cierra el archivo automaticamente al finalizar las operaciones


# 1. Escribe datos inciales (crea (si no existe) o sobreescribe(si existe), para eso es "w", write), lo abrimos como archivo "as archivo"
with open("prueba.txt", "w", encoding = "utf-8") as archivo: 
    archivo.write("primera linea de texto.\n")

# 2. Ahora agregamos, sin borrar lo anterior con "a", append. solo si el archivo existe, si no existe lo crea, al igual que el anterior.
with open("prueba.txt", "a", encoding="utf-8") as archivo:
    archivo.write("segunda linea agregada, sin sobreescribir\n") #el .write es para escribir lo que queremos agregar o crear.

# 3. Ahora, podemos leer o extraer el contenido del archivo con "r", read. lanza error si el archivo no existe
with open("prueba.txt", "r", encoding="utf-8") as archivo:
   for linea in archivo:
    print(linea.strip()) # El .strip() elimina los saltos de linea extra. cuando el archivo es muy grande, es mejor recorrer el contenido con for.
   
   
    """ contenido = archivo.read() # Extrae el contenido de un golpe y lo almacena como un unico objeto tipo str
    print("contenido del archivo:")
    print(contenido) # Imprime el contenido del archivo"""
