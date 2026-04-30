# 'pass' se usa cuando Python necesita que pongas algo de código pero tú no quieres hacer nada todavía.
# 'else' en un bucle es código que se ejecuta SOLO si el bucle terminó bien (sin interrupciones de 'break').

# 1. Ejemplo de pass: un hueco para rellenar después
for i in range(5):
    if i == 2:
        pass # Aquí haré algo en el futuro, por ahora no hace nada
    else:
        print(f"Número {i}")

# 2. Ejemplo de else: buscar algo y avisar si NO se encontró
numeros = [4, 6, 8, 10]
for n in numeros:
    if n == 7:
        print("¡Encontré el 7!")
        break
else:
    # Esto se ejecuta porque nunca llegamos al 'break'
    print("No encontré el número 7 en la lista.")

# 3. Validar una lista con else
edades = [20, 30, 18, 25]
for edad in edades:
    if edad < 18:
        print("Hay alguien menor de edad.")
        break
else:
    print("Todo perfecto: todos son mayores de edad.")

# 4. Uso de else con el bucle while
intentos = 0
while intentos < 3:
    print(f"Intento número {intentos + 1}")
    intentos += 1
    # Si pusiéramos un break aquí, el else no funcionaría
else:
    print("Se terminaron todos los intentos permitidos.")