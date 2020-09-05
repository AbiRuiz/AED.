
nombres = ['Lucas', 'Franco', 'Luciano', 'Malena', 'Jonatan', 'Luciano', 'Rodrigo', 'Maria Sol',
           'Enzo', 'Milena']

# Ejercicio 1

def ejercicio_1_for_en_vector(vector):

    for i in vector:

        print(i)

# Ejercicio 2

def ejercicio_2_for_en_vector(vector):

    for i in range(len(vector)):

        print(f'El nombre: {vector[i]} se encuentra en la posicón: {i + 1}')

# Ejercicio 3

def ejercicio_3_for_en_vector(vector):

    print(vector[1])

    for i in range(5, len(vector)):


        print(vector[i])

#Ejercicio 4

def ejercicio_4_while():

    contador = 0
    acumulador = 0
    nota = int(input(f'Ingrese la nota N°{contador + 1}: '))



    while nota != 0:

        contador = contador + 1
        acumulador = acumulador + nota
        nota = int(input(f'Ingrese la nota N°{contador + 1}: '))

    promedio = acumulador / contador

    print(f'el promedio es: {promedio}')

print('Ejercicio 1: \n')
ejercicio_1_for_en_vector(nombres)
print()

print('Ejercicio 2: \n')
ejercicio_2_for_en_vector(nombres)
print()

print('Ejercicio 3: \n')
ejercicio_3_for_en_vector(nombres)
print()

print('Ejercicio 4: \n')
ejercicio_4_while()
print()


