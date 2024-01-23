# Inicialitzar un diccionari buit per emmagatzemar contactes
diccionari_contactes = {}

while True:
    # Demanar a l'usuari que introdueixi un nom i edat
    nom = input("Introdueix el nom del contacte (o escriu 'stop' per acabar): ")

    # Comprovar si l'usuari vol acabar d'introduir contactes
    if nom.lower() == 'stop':
        break

    edat = int(input(f"Introdueix l'edat de {nom}: "))

    # Comprovar si el nom ja existeix al diccionari
    if nom in diccionari_contactes:
        print(f"El contacte {nom} ja existeix al diccionari. No s'afegirà.")
    else:
        # Afegir el contacte al diccionari
        diccionari_contactes[nom] = edat

# Mostrar el diccionari final amb els contactes
print("Diccionari de contactes:")
for nom, edat in diccionari_contactes.items():
    print(f"{nom}: {edat} anys")
