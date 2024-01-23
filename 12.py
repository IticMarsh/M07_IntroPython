# Inicialitzar una llista buida per emmagatzemar les paraules
llista_paraules = []

# Demanar 10 vegades una paraula diferent a l'usuari
for _ in range(10):
    paraula = input("Introdueix una paraula: ")
    llista_paraules.append(paraula)

# Ordenar la llista alfabèticament
llista_paraules_ordenada = sorted(llista_paraules)

# Mostrar per pantalla la llista ordenada
print("Llista de paraules ordenada alfabèticament:", llista_paraules_ordenada)
