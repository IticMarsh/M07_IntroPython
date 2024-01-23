# Demanar a l'usuari que introdueixi 10 números separats per un espai
entrada_usuari = input("Introdueix 10 números separats per un espai: ")

# Convertir la cadena d'entrada en una llista de números
numeros = [int(num) for num in entrada_usuari.split()]

# Verificar que s'han introduït 10 números
if len(numeros) == 10:
    # Convertir la llista de números en una tupla
    tupla_numeros = tuple(numeros)

    # Ordenar la tupla de menor a major
    tupla_ordenada = tuple(sorted(tupla_numeros))

    # Mostrar per pantalla el contingut de la tupla ordenada
    print("Tupla ordenada de menor a major:", tupla_ordenada)
else:
    print("S'han d'introduir exactament 10 números.")
