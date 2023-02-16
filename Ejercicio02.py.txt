#Ejercicio02
#Creando lista de tareas
tareas = []

#Funcion agregar tarea
def agregar_tarea():
    tarea = input("Ingrese una tarea para agregar al inicio de la lista: ")
    tareas.insert(0, tarea)

#Funcion eliminar tarea
def eliminar_tarea():
    if tareas:
        tarea_eliminada = tareas.pop()
        print(f"Se eliminó la tarea '{tarea_eliminada}' del final de la lista.")
    else:
        print("La lista de tareas está vacía.")

#Funcion mostrar lista de tareas
def mostrar_tareas_invertido():
    if tareas:
        print("Lista de tareas en orden inverso:")
        for tarea in reversed(tareas):
            print(tarea)
    else:
        print("La lista de tareas está vacía.")
#Funcion mostrar numero de tareas
def contar_tareas():
    cantidad_tareas = len(tareas)
    print(f"Hay {cantidad_tareas} tareas en la lista.")

#Prueba de insercion
while True:
    print("\n1. Agregar tarea al inicio de la lista")
    print("2. Eliminar tarea del final de la lista")
    print("3. Mostrar todas las tareas en orden inverso")
    print("4. Contar la cantidad total de tareas en la lista")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        eliminar_tarea()
    elif opcion == "3":
        mostrar_tareas_invertido()
    elif opcion == "4":
        contar_tareas()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente de nuevo.")