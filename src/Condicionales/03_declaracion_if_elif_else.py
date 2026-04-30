# Cuando tenemos más de dos opciones, usamos 'elif' que es como decir "si no es lo anterior, entonces prueba esto".

# Ejemplo 1: Clasificar un número
numero = 0
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Ejemplo 2: Poner una calificación según la nota
nota = 87
if nota >= 90:
    print("Calificación: Sobresaliente")
elif nota >= 80:
    print("Calificación: Notable")
elif nota >= 70:
    print("Calificación: Aprobado")
else:
    print("Calificación: Suspenso")

# Ejemplo 3: Ver en qué etapa de la vida está alguien
edad = 45
if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de 65 años.")

# Ejemplo 4: El 'else' al final no siempre es obligatorio
color = "azul"
if color == "rojo":
    print("El color es rojo.")
elif color == "verde":
    print("El color es verde.")
elif color == "azul":
    print("El color es azul.")