mi_tupla = (1, 3, 2, 5, 6, 5, 6, 8, 5, 6, 1, 2, 3, 2, 6)
while True:
   try:
      entrada = input("Introduce un numero que deseas buscar, o 'salir' para terminar: ")

      if entrada.lower() == 'salir':
         print("Hasta la proxima!")
         break
      
      numero_buscar = int(entrada)
      repeticiones = mi_tupla.count(numero_buscar)

      if repeticiones > 0:
         print(f" El numero {numero_buscar} se repite {repeticiones} veces en la tupla.")
      else:
         print(f"El numero {numero_buscar} no aparece en la tupla.")

   except ValueError:
    print("Por favor, introduce un numero valido o escribe 'salir'.")
          