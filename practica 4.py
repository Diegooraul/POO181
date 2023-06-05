class Bebida:
    def __init__(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio


class AlmacenBebidas:
    def __init__(self):
        self.bebidas = []

    def agregar_bebida(self, bebida):
        self.bebidas.append(bebida)

    def eliminar_bebida(self, id):
        bebidas_actualizadas = [bebida for bebida in self.bebidas if bebida.id != id]
        if len(bebidas_actualizadas) == len(self.bebidas):
            print("No se encontró ninguna bebida con ese ID.")
        else:
            self.bebidas = bebidas_actualizadas
            print("Bebida eliminada correctamente.")

    def actualizar_bebida(self, id, nuevo_precio):
        for bebida in self.bebidas:
            if bebida.id == id:
                bebida.precio = nuevo_precio
                print("Precio actualizado correctamente.")
                return
        print("No se encontró ninguna bebida con ese ID.")

    def mostrar_todas(self):
        if len(self.bebidas) == 0:
            print("No hay bebidas en el almacén.")
        else:
            for bebida in self.bebidas:
                print("ID:", bebida.id)
                print("Nombre:", bebida.nombre)
                print("Clasificación:", bebida.clasificacion)
                print("Marca:", bebida.marca)
                print("Precio:", bebida.precio)
                print("")

    def calcular_precio_promedio(self):
        if len(self.bebidas) == 0:
            return 0
        else:
            total = sum(bebida.precio for bebida in self.bebidas)
            promedio = total / len(self.bebidas)
            return promedio

    def cantidad_bebidas_marca(self, marca):
        cantidad = sum(1 for bebida in self.bebidas if bebida.marca == marca)
        return cantidad

    def cantidad_por_clasificacion(self, clasificacion):
        cantidad = sum(1 for bebida in self.bebidas if bebida.clasificacion == clasificacion)
        return cantidad


# Ejemplo de uso del programa
almacen = AlmacenBebidas()

# Agregar bebidas
bebida1 = Bebida(1, "Agua", "Sin Azúcar", "Marca1", 1.5)
bebida2 = Bebida(2, "Refresco", "Azucarada", "Marca2", 2.0)
bebida3 = Bebida(3, "Energética", "Energética", "Marca1", 3.5)
almacen.agregar_bebida(bebida1)
almacen.agregar_bebida(bebida2)
almacen.agregar_bebida(bebida3)

# Mostrar todas las bebidas
print("Todas las bebidas:")
almacen.mostrar_todas()

# Calcular precio promedio de bebidas
precio_promedio = almacen.calcular_precio_promedio()
print("Precio promedio de bebidas:", precio_promedio)

# Cantidad de bebidas de una marca
cantidad_marca = almacen.cantidad_bebidas_marca("Marca1")
print("Cantidad de bebidas de la marca 'Marca1':", cantidad_marca)

# Cantidad por clasificación
cantidad_clasificacion = almacen.cantidad_por_clasificacion("Azucarada")
print("Cantidad de bebidas con clasificación 'Azucarada':", cantidad_clasificacion)

# Eliminar una bebida
almacen.eliminar_bebida(2)

# Mostrar todas las bebidas después de eliminar una
print("Todas las bebidas después de eliminar una:")
almacen.mostrar_todas()
