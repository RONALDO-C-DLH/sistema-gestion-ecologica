class Pila:
    def __init__(self):
        self._datos = []

    def apilar(self, elemento):
        """Agrega un elemento al tope de la pila."""
        self._datos.append(elemento)

    def desapilar(self):
        """Elimina y retorna el elemento del tope. Error si está vacía."""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._datos.pop()

    def cima(self):
        """Retorna el elemento del tope sin quitarlo. Error si está vacía."""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._datos[-1]

    def esta_vacia(self):
        """Devuelve True si no hay elementos."""
        return len(self._datos) == 0

    def tamano(self):
        """Retorna la cantidad de elementos en la pila."""
        return len(self._datos)
