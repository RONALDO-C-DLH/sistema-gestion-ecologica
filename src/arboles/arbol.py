class NodoArbol:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        """Inserta una clave manteniendo la propiedad del BST."""
        if not self.raiz:
            self.raiz = NodoArbol(clave)
        else:
            self._insertar_rec(self.raiz, clave)

    def _insertar_rec(self, nodo, clave):
        if clave < nodo.clave:
            if nodo.izq:
                self._insertar_rec(nodo.izq, clave)
            else:
                nodo.izq = NodoArbol(clave)
        else:
            if nodo.der:
                self._insertar_rec(nodo.der, clave)
            else:
                nodo.der = NodoArbol(clave)

    def buscar(self, clave):
        """Devuelve True si la clave existe en el árbol, False si no."""
        return self._buscar_rec(self.raiz, clave)

    def _buscar_rec(self, nodo, clave):
        if not nodo:
            return False
        if clave == nodo.clave:
            return True
        if clave < nodo.clave:
            return self._buscar_rec(nodo.izq, clave)
        return self._buscar_rec(nodo.der, clave)
