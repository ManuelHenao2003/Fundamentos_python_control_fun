# El 'if-else' se usa cuando tenemos dos caminos posibles.
# Si se cumple la condición, hace lo del 'if'. Si no se cumple, hace lo del 'else'.

# Ejemplo 1: Saber si alguien puede votar
edad = 17
if edad >= 18:
    print("Puedes votar en las elecciones.")
else:
    print("Aún no tienes edad para votar.")

# Ejemplo 2: Revisar una contraseña
# El usuario escribe algo y nosotros vemos si es igual a la palabra secreta
contrasena = "secreta123" # Aquí imaginamos que el usuario puso esto
if contrasena == "secreta123":
    print("Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")

# Ejemplo 3: Ver si un número es par o impar
# El signo % nos dice cuánto sobra de una división
numero = 15
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Ejemplo 4: Hacer varias cosas si se cumple o no
# Podemos poner más de una línea de código dentro de los bloques
saldo = 300
retiro = 500
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
else:
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")