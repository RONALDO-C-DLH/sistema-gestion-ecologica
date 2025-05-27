class RecursoEcologico:
    def __init__(self, tipo, nombre, ubicacion):
        self.tipo = tipo
        self.nombre = nombre
        self.ubicacion = ubicacion

class NodoArbol:
    def __init__(self, recurso):
        self.recurso = recurso
        self.izquierda = None
        self.derecha = None

class ArbolRecursos:
    def __init__(self):
        self.raiz = None

    def insertar(self, recurso):
        def _insertar(nodo, recurso):
            if not nodo:
                return NodoArbol(recurso)
            if recurso.nombre < nodo.recurso.nombre:
                nodo.izquierda = _insertar(nodo.izquierda, recurso)
            else:
                nodo.derecha = _insertar(nodo.derecha, recurso)
            return nodo
        self.raiz = _insertar(self.raiz, recurso)

    def buscar_por_nombre(self, nombre):
        def _buscar(nodo, nombre):
            if not nodo:
                return None
            if nombre == nodo.recurso.nombre:
                return nodo.recurso
            elif nombre < nodo.recurso.nombre:
                return _buscar(nodo.izquierda, nombre)
            else:
                return _buscar(nodo.derecha, nombre)
        return _buscar(self.raiz, nombre)

    def mostrar_inorden(self):
        def _inorden(nodo):
            if nodo:
                _inorden(nodo.izquierda)
                print(f"{nodo.recurso.nombre} - {nodo.recurso.tipo} - {nodo.recurso.ubicacion}")
                _inorden(nodo.derecha)
        _inorden(self.raiz)
