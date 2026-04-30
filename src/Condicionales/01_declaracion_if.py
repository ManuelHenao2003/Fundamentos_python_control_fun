# La declaración if sirve para que el programa tome decisiones.
# Si lo que ponemos al lado del 'if' es verdad, entonces se hace lo que está adentro.

# Ejemplo 1: Ver si alguien es mayor de edad
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")

# Ejemplo 2: Ver si hace calor
temperatura = 30
if temperatura > 25:
    print("Hace calor hoy.")

# Ejemplo 3: Usar 'and' para que se cumplan dos cosas a la vez
# Queremos que la hora esté entre las 6 y las 12
hora = 10
if hora >= 6 and hora < 12:
    print("Buenos días.")