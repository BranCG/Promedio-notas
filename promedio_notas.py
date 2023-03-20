notas = []

print("BIENVENIDO A CALCULO DE PROMEDIOS INACAP")

while True:  # Creamos un bucle infinito con While True
    nota = input(
        "Ingresar notas del estudiante (1.0 - 7.0), o 's' para salir: ")  # Pedimos info al usuario con input
    if nota == 's':
        break  # Paramos la aplicacion si se envia la letra s
    try:  # Para generar un ValueError al final
        nota = float(nota)  # Tipamos la nota con Float para dar valor decimal
        if nota < 1.0 or nota > 7.0:  # Este if devuelve el print si si se cumplen estas condiciones
            print("Error: la nota debe estar entre 1.0 y 7.0")
        else:
            # Append agregara la nota en caso de que se ingrese
            notas.append(nota)
    # Se usa para dar error a un valor que no sea valido, como al ingresar un str.
    except ValueError:
        print("Error: entrada inválida")

if len(notas) == 0:
    print("No se ingresaron notas")
else:
    # Si se ingresan notas se realiza el calculo normalmente.
    promedio = sum(notas) / len(notas)
    # el .1f sirve para dar 1 numero decimal en el float
    print(f"El promedio de notas es: {promedio:.1f}")
