class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        """Inserta un elemento al inicio de la lista."""
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def buscar(self, dato):
        """Devuelve True si el elemento existe en la lista."""
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, dato):
        """Elimina la primera ocurrencia del dato y retorna True. Si no existe, False."""
        prev = None
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                if prev:
                    prev.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            prev = actual
            actual = actual.siguiente
        return False

    def recorrer(self):
        """Itera sobre todos los elementos de la lista."""
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente
