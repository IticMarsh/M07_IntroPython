# Demanar a l'usuari que introdueixi una paraula o frase
paraula_o_frase = input("Introdueix una paraula o frase: ")

# Eliminar espais en blanc i convertir tot a minúscules per a la comprovació
paraula_o_frase = paraula_o_frase.replace(" ", "").lower()

# Verificar si la paraula o frase és capicua (palíndrom)
if paraula_o_frase == paraula_o_frase[::-1]:
    print("És una paraula o frase capicua (palíndrom).")
else:
    print("No és una paraula o frase capicua (palíndrom).")
