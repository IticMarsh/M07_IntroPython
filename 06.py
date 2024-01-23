# Demanar a l'usuari que introdueixi entre 2 i 3 paraules
paraules = input("Introdueix entre 2 i 3 paraules separades per espais: ")

# Separar les paraules
llista_paraules = paraules.split()

# Comprovar que s'han introduït entre 2 i 3 paraules
if 2 <= len(llista_paraules) <= 3:
    # Mostrar les paraules
    print(f"Paraules introduïdes: {', '.join(llista_paraules)}")

    # Calcular i mostrar la longitud de les paraules
    for paraula in llista_paraules:
        print(f"Longitud de '{paraula}': {len(paraula)} caràcters")

        # Mostrar el primer i últim caràcter de cada paraula
        print(f"Primer caràcter de '{paraula}': {paraula[0]}")
        print(f"Últim caràcter de '{paraula}': {paraula[-1]}")
else:
    print("S'ha de introduir entre 2 i 3 paraules.")
