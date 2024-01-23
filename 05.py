# Demanar a l'usuari que introdueixi el valor en euros
valor_euros = float(input("Introdueix el valor en euros: "))

# Demanar a l'usuari que introdueixi el percentatge d'IVA (4%, 10% o 21%)
iva_percentatge = float(input("Introdueix el percentatge d'IVA (4, 10 o 21%): "))

# Calcular l'IVA
iva = (iva_percentatge / 100) * valor_euros

# Calcular el valor final amb l'IVA afegit
valor_final = valor_euros + iva

# Mostrar els resultats per pantalla
print(f"Valor introduït: {valor_euros} €")
print(f"Percentatge d'IVA: {iva_percentatge}%")
print(f"Valor final amb l'IVA afegit: {valor_final} €")
