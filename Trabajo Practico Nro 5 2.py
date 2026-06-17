numeros = []
while True:
    try:
        numero = int(input("Ingrese un numero (0 para terminar): "))
        if numero == 0:
            break
        numeros.append(numero)
    except ValueError:
     print("Por Favor, introduce un numero valido.")
numeros.sort()
print("\nNumeros ordenados de menor a mayor:")
print(numeros)