from Metodos import cargar_notas,mostrar_nota,alumnos_promocionados,porcentajes,mejor_promedio

def menu():

    print('----------------')
    print('      Menú')
    print('----------------')
    print('1. Cargar un alumno y su nota: ')
    print('2. Mostrar el listado de las notas: ')
    print('3. Mostrar el listado de los alumnos promocionados: ')
    print('4. Mostrar el porcentaje de alumnos reprobados, aprobados y promocionados: ')
    print('5. Mostrar los 3 alumnos con mejor promedio: ')
    print()
    print('0. Finalizar')
    print()

    op = int(input('Ingrese la opción seleccionada: '))

    if op < 0 or op > 5:

        print('Error! ingrese un valor valido.')
        print()
        input('Presione enter para volver al menú.')
        menu()

    if op == 1:

        cargar_notas(lista_alumnos_notas)
        input('Presione enter para volver al menú.')
        menu()

    elif op == 2:

        check(lista_alumnos_notas)
        mostrar_nota(lista_alumnos_notas)
        input('Presione enter para volver al menú')
        menu()

    elif op == 3:

        check(lista_alumnos_notas)
        alumnos_promocionados(lista_alumnos_notas)
        input('Presione enter para volver al menú')
        menu()

    elif op == 4:

        check(lista_alumnos_notas)
        porcentajes(lista_alumnos_notas)
        input('Presione enter para volver al menú')
        menu()


    elif op == 5:

        mejor_promedio(lista_alumnos_notas)
        input('Presione enter para volver al menú')
        menu()


    else:

        exit()

def check(lista):

    if len(lista) == 0:

        print('¡Error! No hay elementos cargados en la lista de alumnos y sus notas')
        print()
        input('Presione enter para volver al menú')
        menu()


# Bloque principal

lista_alumnos_notas = []
menu()