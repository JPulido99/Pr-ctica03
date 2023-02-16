# Ejercicio 01
# Creando lista vacía
lista_compras = []

# Función agregar producto adelante
def add_producto(producto):
    lista_compras.append(producto)
    print(f"{producto} ha sido agregado a la lista de compras.")

# Función eliminar último producto
def delete_producto():
    if len(lista_compras) > 0:
        producto_eliminado = lista_compras.pop(0)
        print(f"{producto_eliminado} ha sido eliminado de la lista de compras.")
    else:
        print("La lista está vacía.")

# Función mostrar productos de lista
def mostrar_lista():
    if len(lista_compras) > 0:
        print("Lista de compras:")
        for i, producto in enumerate(lista_compras, start=1):
            print(f"{i}. {producto}")
    else:
        print("La lista está vacía.")

# Prueba
add_producto("Carro")
add_producto("Perro")
add_producto("Casa")
mostrar_lista()
delete_producto()
mostrar_lista()