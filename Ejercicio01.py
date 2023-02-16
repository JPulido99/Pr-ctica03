# Inicializar la lista de compras vacía
lista_de_compras = []

# Función para agregar un producto al final de la lista
def agregar_producto(producto):
    lista_de_compras.append(producto)
    print(f"{producto} ha sido agregado a la lista de compras.")

# Función para eliminar el primer producto de la lista
def eliminar_producto():
    if len(lista_de_compras) > 0:
        producto_eliminado = lista_de_compras.pop(0)
        print(f"{producto_eliminado} ha sido eliminado de la lista de compras.")
    else:
        print("La lista de compras está vacía.")

# Función para mostrar todos los productos en la lista en orden de compra
def mostrar_lista():
    if len(lista_de_compras) > 0:
        print("Lista de compras:")
        for i, producto in enumerate(lista_de_compras, start=1):
            print(f"{i}. {producto}")
    else:
        print("La lista de compras está vacía.")

# Ejemplo de uso
agregar_producto("Manzanas")
agregar_producto("Leche")
agregar_producto("Pan")
mostrar_lista()
eliminar_producto()
mostrar_lista()