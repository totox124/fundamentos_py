#aqui haremos una calculadora para IMC
# Necesitamos la altura, y el peso de la persona, para ello requerimos inputs y variables

Peso = float(input("Por favor, indique su peso: "))
altura = float(input("Por favor, indique su altura en metros: "))
resultado = Peso / altura**2
imc = round(resultado, 1)

if imc < 18.5:
    print(f"su imc es de {imc}, se encuentra bajo peso")
elif imc < 25:
    print(f"su imc es de {imc}, se encuentra en peso normal")
elif imc < 30:
    print(f"su imc es {imc}, esta con sobrepeso")
elif imc >= 30:
    print(f"su imc es {imc}, usted se encuentra en algun grado de obesidad")