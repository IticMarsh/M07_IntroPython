# Demanar a l'usuari que introdueixi una frase
frase = input("Introdueix una frase: ")

# Eliminar els espais en blanc de la frase
frase_sense_espais = frase.replace(" ", "")

# Mostrar la frase sense espais per pantalla
print(f"Frase sense espais: {frase_sense_espais}")
