class GestorTareas:
    """Gestion simple de tareas pendientes."""

    def __init__(self):
        self.tareas = []  # Lista de diccionarios {'descripcion': str, 'completada': bool}

    def agregar_tarea(self, descripcion: str) -> None:
        """Agrega una nueva tarea al gestor."""
        self.tareas.append({"descripcion": descripcion, "completada": False})

    def completar_tarea(self, indice: int) -> bool:
        """Marca una tarea como completada por su índice."""
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True
            return True
        return False

    def eliminar_tarea(self, indice: int) -> bool:
        """Elimina una tarea por su índice."""
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)
            return True
        return False

    def obtener_tareas(self):
        """Devuelve la lista de tareas."""
        return self.tareas
