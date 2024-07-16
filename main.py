from nodo import LinkedList
from tarea import Tarea


def main():
    lista_tareas = LinkedList()

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Buscar tarea")
        print("4. Tareas pendientes")
        print("5. Marcar tarea como completada")
        print("6. Mostrar tareas completadas")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            # Agregar tarea
            nombre = input("Ingrese nombre de tarea: ")
            descripcion = input("Ingrese la descripción de tarea: ")
            nueva_tarea = Tarea(nombre, descripcion)
            lista_tareas.insert(nueva_tarea)
            print("Tarea agregada!")

        elif opcion == "2":
            # Eliminar tarea
            nombre_tarea = input(
                "Ingrese nombre de tarea que desea eliminar: ")
            if lista_tareas.delete(nombre_tarea):
                print("Tarea eliminada!")
            else:
                print("La tarea no se encontró.")

        elif opcion == "3":
            # Buscar tarea
            nombre_tarea = input("Ingrese el nombre de la tarea a buscar: ")
            tarea_buscada = lista_tareas.search(nombre_tarea)
            if tarea_buscada is not None:
                print(
                    f"Tarea encontrada: {tarea_buscada.nombre}, Descripción: {tarea_buscada.descripcion}")
            else:
                print("La tarea no se encontró en la lista.")

        elif opcion == "4":

            print("\nTareas pendientes:")
            lista_tareas.show_pending_tasks()

        elif opcion == "5":
            # Marcar tarea como completada
            nombre_tarea = input(
                "Ingrese el nombre de la tarea a marcar como completada: ")
            if lista_tareas.mark_as_completed(nombre_tarea):
                print("Tarea marcada como completada!")
            else:
                print("La tarea no se encontró en la lista.")

        elif opcion == "6":
            # Mostrar tareas completadas
            print("\nTareas completadas:")
            completed_tasks = lista_tareas.show_completed_tasks()
            if completed_tasks:
                for tarea in completed_tasks:
                    print(
                        f"Nombre: {tarea.nombre}, Descripción: {tarea.descripcion}")
            else:
                print("No hay tareas completadas.")

        else:
            print("Opción inválida. Intente nuevamente.")

        # Opción para salir del programa
        salir = input("\n¿Desea salir? (s/n): ")
        if salir.lower() == "s":
            break

    print("Saliendo del programa...")


if __name__ == "__main__":
    main()
