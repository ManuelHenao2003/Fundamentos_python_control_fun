# La evaluación de cortocircuito es cuando Python deja de revisar condiciones si ya sabe la respuesta.

# 1. Con 'and': Si la primera es mentira, ya no mira la segunda
lista = []
# Aquí no da error porque como la lista está vacía, la primera parte es False y ya no intenta leer lista[0]
if lista and lista[0] == 'Python':
    print("El primer elemento es 'Python'.")

# 2. Evitar divisiones por cero
dividendo = 10
divisor = 0
# Si divisor es 0, la primera parte falla y Python no intenta dividir
if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")

# 3. Con 'or': Si la primera es verdad, ya no mira la segunda
acceso_permitido = True
acceso_registrado = False # Imagina que esto cambia algo importante
if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")
    # Como acceso_permitido es True, Python ni tocó a acceso_registrado

# 4. Usando any() y all()
# any(): se para en cuanto encuentra un True
numeros = [0, 0, 1, 0]
if any(numeros):
    print("Al menos un número es no cero.")

# all(): se para en cuanto encuentra un False
condiciones = [True, True, False, True]
if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")