# Ahora, empezaremos con funciones

def operacion(num1, num2):
    resultado = num1 + num2
    return f"el resultado es {resultado}"
while True:
    try:
        x = int(input("ingrese el primer valor: "))
        break                                           # Este break es para que salga de este bucle a la hora de obtener "x" exitosamente
    except ValueError:
            print("solo numeros enteros")
while True:                                         # Esto es para que, si ocurre una exception en el segundo numero, no se repita todo el bucle
    try:
        y = int(input("ingrese el segundo valor: "))
        break                                       # cumple la misma funcion que el break anterior
    except ValueError:
        print("solo numeros enteros")
        
    
    
    
print(operacion(x, y))