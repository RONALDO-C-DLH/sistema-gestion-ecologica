from collections import deque

class Grafo:
    def __init__(self):
        self.adj = {}

    def agregar_vertice(self, v):
        """Agrega un vértice al grafo si no existe."""
        if v not in self.adj:
            self.adj[v] = []

    def agregar_arista(self, u, v):
        """Agrega una arista no dirigida entre u y v."""
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, inicio):
        """Recorrido en anchura desde un vértice inicial."""
        visitados = set([inicio])
        cola = deque([inicio])
        recorrido = []
        while cola:
            v = cola.popleft()
            recorrido.append(v)
            for w in self.adj[v]:
                if w not in visitados:
                    visitados.add(w)
                    cola.append(w)
        return recorrido

    def dfs(self, inicio, visitados=None, recorrido=None):
        """Recorrido en profundidad desde un vértice inicial."""
        if visitados is None:
            visitados = set()
            recorrido = []
        visitados.add(inicio)
        recorrido.append(inicio)
        for w in self.adj[inicio]:
            if w not in visitados:
                self.dfs(w, visitados, recorrido)
        return recorrido
