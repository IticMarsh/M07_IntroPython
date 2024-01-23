# Demanar a l'usuari que introdueixi 10 números separats per espais
entrada_usuari = input("Introdueix 10 números separats per espais: ")

# Convertir la cadena d'entrada en una llista de números
numeros = [float(num) for num in entrada_usuari.split()]

# Calcular la suma dels números i la mitjana
suma_total = sum(numeros)
mitjana = suma_total / len(numeros)

# Afegir la suma total i la mitjana a la llista
numeros.extend([suma_total, mitjana])

# Mostrar per pantalla la llista i els resultats
print("Números de l'usuari:")
print(numeros[:-2])  # Mostrar la llista sense la suma total i la mitjana
print("Suma total:", suma_total)
print("Mitjana:", mitjana)
