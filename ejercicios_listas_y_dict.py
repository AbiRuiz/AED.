
def ejercicio_1_cargar_lista():

    lista_alumnos = []

    for x in range(10):

        nombre = input("Ingrese el nombre del alumno que desea cargar: ")
        lista_alumnos.append(nombre)

    for x in range(len(lista_alumnos)):

        print(lista_alumnos[x])

def ejercicio_2_modificar_lista():

    frutas = ['manzana', 'peras', 'durazno']
    verduras = ['acelga', 'lechuga']

    fruta_nueva = input('ingrese una nueva fruta: ')

    frutas.insert(2, fruta_nueva)

    print(frutas)

    verduras.extend(frutas)

    print(verduras)

    verduras.remove(fruta_nueva)

    print(verduras)

    frutas.pop(-1)

    print(frutas)

def ejercicio_3_ordenar_y_buscar_lista():

    years = [1998, 1989, 1970, 2020, 1990]

    print(years)

    years.sort()

    print(years)

    search_year = int(input('Ingrese un año: '))

    if search_year in years:

        print('El año ingresado se encuentra ya en la lista de años')

    else:

        print('El año ingresado no se encuetra en la lista de años')

    print(years.index(1989))

def ejercico_4_diccionarios():

    jugador = {
        'comida': 15,
        'energía': 100,
        'enemigos': 3
    }

    print(jugador)
    print()

    for x in jugador:
        print(x)

    print()

    jugador['nuevas armas'] = {
        'rocas' : 4,
        'flechas' : 5
    }

    for x in jugador:
        item = jugador[x]
        print(f'{x}: {item}')

    jugador["amigos"] = 10
    print()
    for x in jugador:
        item = jugador[x]
        print(f'{x}: {item}')

    jugador["comida"] = 30

    print()

    for x in jugador:
        item = jugador[x]
        print(f'{x}: {item}')

    print()

    x = jugador["energía"]

    print(x)

ejercicio_1_cargar_lista()

ejercicio_2_modificar_lista()

ejercicio_3_ordenar_y_buscar_lista()

ejercico_4_diccionarios()