class Cola:
    def __init__(self):
        self._datos = []

    def encolar(self, elemento):
        """Agrega un elemento al final de la cola."""
        self._datos.append(elemento)

    def desencolar(self):
        """Elimina y retorna el primer elemento. Error si está vacía."""
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._datos.pop(0)

    def frente(self):
        """Retorna el primer elemento sin quitarlo. Error si está vacía."""
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._datos[0]

    def esta_vacia(self):
        """Devuelve True si no hay elementos."""
        return len(self._datos) == 0

    def tamano(self):
        """Retorna la cantidad de elementos en la cola."""
        return len(self._datos)
