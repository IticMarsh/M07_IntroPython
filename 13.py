# Demanar a l'usuari que introdueixi dues paraules
paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

# Afegir les paraules a una llista
llista_paraules = [paraula1, paraula2]

# Inicialitzar un diccionari per comptar les vegades que apareix cada lletra
comptador_lletres = {}

# Recórrer les paraules de la llista
for paraula in llista_paraules:
    # Recórrer les lletres de cada paraula
    for lletra in paraula:
        # Incrementar el comptador per aquesta lletra
        comptador_lletres[lletra] = comptador_lletres.get(lletra, 0) + 1

# Mostrar per pantalla quantes vegades apareix cada lletra
print("Comptador de lletres:")
for lletra, comptador in comptador_lletres.items():
    print(f"{lletra}: {comptador} vegades")
