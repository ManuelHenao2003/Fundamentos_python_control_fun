# El 'return' es lo que la función nos devuelve al terminar su trabajo.
# También sirve para que la función se pare inmediatamente.

# 1. Ejemplo básico de devolución de valor
def cuadrado(n):
    return n * n

resultado = cuadrado(4)
print(f"Cuadrado de 4: {resultado}")

# 2. Devolver varios valores a la vez (Python los agrupa en una tupla)
def estadisticas(numeros):
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return suma, promedio

total, media = estadisticas([10, 20, 30])
print(f"Suma: {total}, Media: {media}")

# 3. 'return' temprano (para salir rápido si hay un error)
def dividir_seguro(a, b):
    if b == 0:
        print("¡No se puede dividir por cero!")
        return None # Salimos de la función aquí mismo
    return a / b

print(f"10/2 = {dividir_seguro(10, 2)}")
print(f"10/0 = {dividir_seguro(10, 0)}")

# 4. Devolver valores booleanos (True o False)
def es_mayor(edad):
    return edad >= 18

if es_mayor(20):
    print("Es mayor de edad")

# 5. Devolver listas o diccionarios
def lista_pares(limite):
    return [x for x in range(0, limite + 1, 2)]

print(f"Pares hasta 10: {lista_pares(10)}")