from tarea import Tarea

# Creamos una clase Node con la propiedad tarea y un puntero


class Node:
    def __init__(self, tarea):
        self.tarea = tarea
        self.next = None


# Creamos la clase LinkedList que inicializa con la propiedad cabecera en None.
# Se inicia una lista para almacenar las tareas completadas.


class LinkedList:
    def __init__(self):
        self.head = None
        self.completed_tasks = []


# El método insertar agrega una tarea a la lista enlazada tomando como argumentos una instancia de Node...
# con su nombre y descripción (que a su vez la toma de una instancia de Tarea).

    def insert(self, tarea):
        new_node = Node(tarea)
        if self.head is None:  # Se verifica si la lista está vacía,
            # En cuyo caso el nuevo nodo será cabecera.
            self.head = new_node
        else:  # Si ya hay una cabecera,entonces...
            # Se crea una variable temporal con el head como contenido.
            current_node = self.head
            # Se recorren los nodos hasta el último (puntero sea None).
            while current_node.next is not None:
                current_node = current_node.next  # Mientras se recorren
            current_node.next = new_node  # Se enlaza con el nodo anterior

    def delete(self, nombre_tarea):  # Crea un método para eliminar tareas agendadas
        # Se comienza en current_node = self.head para dar el inicio desde la cabecera, así en los demás métodos.
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.tarea.nombre == nombre_tarea:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                del current_node
                return True
            previous_node = current_node
            current_node = current_node.next
        return False

    # Crea un método para buscar por el nombre de una tarea en la lista enlazada
    def search(self, nombre_tarea):
        current_node = self.head
        while current_node is not None:
            if current_node.tarea.nombre == nombre_tarea:
                return current_node.tarea
            current_node = current_node.next
        return None

    # Una vez tenemos al menos un nodo, éste método nos permite mostrar los nombres de las tareas pendientes.
    def show_pending_tasks(self):
        current_node = self.head
        while current_node is not None:
            if not current_node.tarea.completada:
                print(f"Tarea: {current_node.tarea.nombre}")
            current_node = current_node.next

    # Este método nos permiten marcar como completada una tarea y almacenarla en una lista iniciado por __init__
    def mark_as_completed(self, nombre):
        current_node = self.head
        while current_node is not None:
            if current_node.tarea.nombre == nombre:
                current_node.tarea.completada = True
                self.completed_tasks.append(current_node.tarea)
                return True
            current_node = current_node.next
        return False

    # Muestra los datos almacenados en la lista de tareas completadas.
    def show_completed_tasks(self):
        return self.completed_tasks
