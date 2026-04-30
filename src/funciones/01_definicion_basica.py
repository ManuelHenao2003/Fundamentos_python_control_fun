# Las funciones son como pequeñas recetas de código que podemos guardar para usar después.
# Se definen con la palabra 'def' y así no tenemos que escribir lo mismo muchas veces.

# 1. Una función muy simple que solo saluda
def saludar():
    print("¡Hola, mundo!")

# Para que funcione, hay que "llamarla" así:
saludar()

# 2. Función con cálculos (área de un rectángulo)
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Guardamos el resultado en una variable
resultado = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {resultado}")

# 3. Función para saber si un número es par
def es_par(numero):
    return numero % 2 == 0

print(f"¿Es 10 par?: {es_par(10)}")

# 4. Guardar una función en una variable
# Es como darle otro nombre a la misma "receta"
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

convertir = celsius_a_fahrenheit
print(f"25°C en Fahrenheit son: {convertir(25)}")

# 5. El "alcance" (scope) de las variables
def ejemplo_alcance():
    texto_interno = "Solo existo aquí dentro"
    return texto_interno

# print(texto_interno) # Esto daría error porque la variable está encerrada en la función
print(ejemplo_alcance())