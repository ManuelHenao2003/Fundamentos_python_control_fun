# Los docstrings son textos para explicar qué hace una función.
# Se ponen justo debajo de la definición usando tres comillas.

# 1. Una explicación corta
def sumar(a, b):
    """Suma dos números y devuelve el total."""
    return a + b

# 2. Una explicación más detallada (Estilo Google)
def calcular_promedio(numeros):
    """
    Calcula la media de una lista de números.

    Argumentos:
        numeros: Una lista con números.

    Devuelve:
        El promedio (float).
    """
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

# 3. Cómo ver la documentación de una función
# Podemos usar help() o el atributo __doc__
print("Explicación de la función sumar:")
print(sumar.__doc__)

# help(calcular_promedio) # Descomenta esto para verlo en la terminal

# 4. Incluir ejemplos en la documentación (doctest)
def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Ejemplos:
        >>> area_triangulo(10, 5)
        25.0
    """
    return (base * altura) / 2

print(f"Área: {area_triangulo(10, 5)}")