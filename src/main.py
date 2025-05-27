from pilas.pila import Pila
from colas.cola import Cola
from listas.lista import ListaEnlazada
from arboles.arbol import ArbolBinarioBusqueda
from grafos.grafo import Grafo

def main():
    # Prueba de Pila
    p = Pila()
    p.apilar("Campaña A")
    p.apilar("Campaña B")
    print("Cima de la pila:", p.cima())  # Debe mostrar "Campaña B"

    # Prueba de Cola
    c = Cola()
    c.encolar("Solicitud 1")
    c.encolar("Solicitud 2")
    print("Frente de la cola:", c.frente())  # Debe mostrar "Solicitud 1"

    # Prueba de Lista Enlazada
    l = ListaEnlazada()
    l.insertar("Punto Limpio 1")
    l.insertar("Área Verde 1")
    print("Recorrido de la lista:", list(l.recorrer()))
    # Debe mostrar ['Área Verde 1', 'Punto Limpio 1']

    # Prueba de Árbol de Búsqueda Binario
    a = ArbolBinarioBusqueda()
    for clave in ["Parque", "Bosque", "Jardín"]:
        a.insertar(clave)
    print("¿Existe 'Jardín'?", a.buscar("Jardín"))  # Debe mostrar True

    # Prueba de Grafo
    g = Grafo()
    g.agregar_arista("Grupo A", "Grupo B")
    g.agregar_arista("Grupo B", "Grupo C")
    print("Recorrido BFS desde 'Grupo A':", g.bfs("Grupo A"))
    # Debe mostrar ['Grupo A', 'Grupo B', 'Grupo C']

if __name__ == "__main__":
    main()
