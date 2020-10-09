""" Una empresa de alquiler de autos necesita un programa que le permita cargar los alquiles realizados,
los datos (atributos) que se desean registrar por cada alquiler son: Marca, modelo, año, precio por Kilómetro,
Seguro Alquiler, DNI del arrendatario (quien alquila el vehículo), Nombre del arrendatario y kilómetros recorridos.

Los métodos que se deberán crear en esta clase son: cargar alquiler(init constructor),
mostrar alquiler (print de todos los atributos) ademas de mostrar todos los datos
deberá mostrar el monto calculado del alquiler (precio_por_km*km_recorridos+seguro_alquiler).

Cree un programa modular que permita cargar una lista de alquileres, Con las siguientes opciones:
1. Cargar un nuevo Alquiler en la lista
2. Mostrar la lista de alquileres
0. Finalizar
"""

class Alquiler:

       def __init__(self, marca, modelo, año, precio_por_km, seguro_alquiler, dni_del_arrendatario, nombre_del_arrendatario, km_recorridos):

           self.marca = marca
           self.modelo = modelo
           self.año = año
           self.precio_por_km = precio_por_km
           self.seguro_alquiler = seguro_alquiler
           self.dni_del_arrendatario = dni_del_arrendatario
           self.nombre_del_arrendatario = nombre_del_arrendatario
           self.km_recorridos = km_recorridos


       def mostrar_alquiler(self):

           print(f'Marca: {self.marca}')
           print(f'Modelo: {self.modelo}')
           print(f'Año: {self.año}')
           print(f'Precio por Kilometro: {self.precio_por_km}')
           print(f'Seguro alquiler: {self.seguro_alquiler}')
           print(f'DNI del arrendatario: {self.dni_del_arrendatario}')
           print(f'Nombre del arrendatario: {self.nombre_del_arrendatario}')
           print(f'Kilometros recorridos: {self.km_recorridos}')
           print(f'Monto total: {self.km_recorridos * self.precio_por_km + self.seguro_alquiler}')

