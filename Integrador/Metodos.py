"""Realice un programa con dos archivos .py, uno que contenga los métodos y otro que contenga al
menú principal
En el menú se debe crear una lista para ingresar las notas del final de los alumnos de AED I

Las opciones deben permitir realizar las tareas listadas a continuación:
1. Cargar una nota: esta opción debe agregar un nuevo registro en la lista
2. Mostrar el listado de las notas: esta opción debe recorrer la lista y mostrar las notas cargadas
3. Mostrar el listado de los alumnos promocionados: esta opción debe llamar a un método sin retorno
y que reciba como parámetro la lista cargada en el punto anterior y muestre las notas mayores o iguales
a 7 con su respectivo indice.
4. Esta opción debe llamar a un método que reciba como parámetro la lista cargada y muestre el porcentaje
de reprobados (nota menor a 4), regulares (nota igual o mayor a cuatro y menor que 7)
y promocionados (nota mayor a 7)
5. Método sin parámetro y sin retorno que solicite cargar los 3 alumnos con el mejor promedio en un
diccionario de datos, donde la key es el nombre del alumno y el valor de la key su calificación.
Una vez cargado el diccionario imprimir en pantalla todos los items del mismo, ejemplo:
abanderados = {Luis: 10, 'Maria': 9.5, 'Jose':9}

Para salir del sistema se debe agregar la opción “0”."""

def cargar_notas(lista):

    nombre = input('Ingrese el nombre del alumno: ')
    nota = int(input('Ingrese la nota del alumno: '))
    print()

    alumno = [nombre,nota]
    lista.append(alumno)

    print('La nota ha sido añadida con exito!')
    print()

def mostrar_nota(lista):

    for i in range(len(lista)):

        print(f'Nombre: {lista[i][0]}')
        print(f'Nota: {lista[i][1]}')

def alumnos_promocionados(lista):

    for i in range(len(lista)):

        if lista[i][1] >= 7:

            print(f'El alumno: {lista[i][0]} está promocionado.')

        else:

            print(f'No hay alumnos promocionados.')

def porcentajes(lista):

    reprobados = 0
    regulares = 0
    promocionados = 0

    for i in range(len(lista)):

        if lista[i][1] >= 7:

            promocionados += 1

        elif lista[i][1] >= 4:

            regulares += 1

        else:

            reprobados += 1

    total = len(lista)

    print(f'Porcentaje de alumnos reprobados: {(reprobados * 100) / total}%')
    print(f'Porcentaje de alumnos regulares: {(regulares * 100) / total}%')
    print(f'Porcentaje de alumnos promocionados: {(promocionados * 100) / total}%')

def mejor_promedio(lista):

    mejorpromedio = {}

    for i in range (3):

        nombre = input('Ingrese el nombre del alumno con mejor promedio: ')
        promedio = int(input('Ingrese el promedio del alumno con mejor promedio: '))

        mejorpromedio[nombre] = promedio

    print(mejorpromedio)
