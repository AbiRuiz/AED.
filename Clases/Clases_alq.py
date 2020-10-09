from Clases_ej import Alquiler

def menu():

    print('1. Cargar un nuevo alquiler a la lista.')
    print('2. Mostrar la lista de alquileres.')
    print('0. Finalizar')
    print()

    op = int(input('Ingrese la opción seleccionada: '))

    if op < 0 or op > 2:

        print('Error! ingrese un valor valido. (1, 2 o 0)')

        input('Para volver al menu presione enter')
        menu()

    if op == 1:

        cargar_alquiler()

    elif op == 2:

        mostrar_listas()

    else:

        print('Fin del programa.')
        print()
        exit()

def cargar_alquiler():

    marca = input('Ingrese la marca del auto que va a alquilar: ')
    modelo = input('Ingrese el modelo del auto que va a alquilar: ')
    año = int(input('Ingrese de que año es auto que va a alquilar: '))
    precio = int(input('Ingrese el precio por kilometro del auto: '))
    seguro = int(input('Ingrese el valor del seguro del auto: '))
    dni = int(input('Ingrese el dni del arrendatario: '))
    nombre = (input('Ingrese el nombre del arrendatario: '))
    kilometros = int(input('Ingrese los kilometros que va a recorrer: '))

    alquiler = Alquiler(marca, modelo, año, precio, seguro, dni, nombre, kilometros)
    alquileres.append(alquiler)

    print()
    print('Se ha cargado con exito el alquiler')
    print()
    input('Presione enter para volver al menu principal.')
    menu()

# Funcion para mostrar la lista de alquileres

def mostrar_listas():

    if len(alquileres) == 0:

        print('La lista de alquileres esta vacia.')
        input('Presione Enter para volver al Menú.')
        print()
        menu()

    else:

        for i in range (len(alquileres)):

            print()
            print(f'Alquiler número: {i+1}')
            print('-------------------------')
            alquileres[i].mostrar_alquiler()
            print()

# Bloque principal

alquileres = []
menu()

