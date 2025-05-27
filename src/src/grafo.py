from collections import defaultdict

class GrafoIniciativas:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_iniciativa(self, nombre):
        if nombre not in self.grafo:
            self.grafo[nombre] = []

    def conectar_iniciativas(self, a, b):
        self.grafo[a].append(b)
        self.grafo[b].append(a)

    def mostrar_conexiones(self):
        for iniciativa, conexiones in self.grafo.items():
            print(f"{iniciativa} se conecta con: {', '.join(conexiones)}")

    def buscar_conexiones(self, inicio):
        visitados = set()
        resultado = []

        def dfs(nodo):
            if nodo not in visitados:
                visitados.add(nodo)
                resultado.append(nodo)
                for vecino in self.grafo[nodo]:
                    dfs(vecino)

        dfs(inicio)
        return resultado
