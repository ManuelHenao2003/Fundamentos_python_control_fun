# El bucle 'for' sirve para recorrer cosas que tienen varios elementos, como listas o palabras.
# También usamos 'range' para repetir algo un número de veces.

# 1. Recorrer una lista de frutas
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# 2. Usar range() para contar
# Esto cuenta del 0 al 4 (el 5 no se incluye)
for i in range(5):
    print(f"Número: {i}")

# 3. range con inicio, fin y salto
print("Contando del 2 al 10 de dos en dos:")
for i in range(2, 11, 2):
    print(i, end=" ")
print() # Salto de línea

# 4. Saber la posición (índice) mientras recorremos
nombres = ["Ana", "Carlos", "Elena"]
for indice, nombre in enumerate(nombres):
    print(f"En la posición {indice} está {nombre}")

# 5. Recorrer una palabra letra por letra
for letra in "Python":
    print(letra)

# 6. Recorrer un diccionario (como una lista con nombres y valores)
usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# 7. Listas rápidas (comprensión de listas)
# Creamos una lista de cuadrados del 1 al 5 en una sola línea
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados: {cuadrados}")

# 8. Un bucle dentro de otro (bucles anidados)
# Hacemos una mini tabla de multiplicar
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()