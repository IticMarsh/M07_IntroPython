# Crear una tupla amb els mesos de l'any
mesos = ('', 'Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Setembre', 'Octubre', 'Novembre', 'Desembre')

# Demanar a l'usuari que posi un número entre 0 i 12
num_mes = int(input("Introdueix un número entre 1 i 12: "))

# Comprovar que el número està dins del rang vàlid
if 1 <= num_mes <= 12:
    # Mostrar per pantalla el mes corresponent al número indicat per l'usuari
    print(f"El mes corresponent al número {num_mes} és: {mesos[num_mes]}")
else:
    print("Número no vàlid. Introdueix un número entre 1 i 12.")
