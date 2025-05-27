import tkinter as tk
from tkinter import messagebox, simpledialog
from pilas.pila import Pila
from colas.cola import Cola
from listas.lista import ListaEnlazada
from arboles.arbol import ArbolBinarioBusqueda
from grafos.grafo import Grafo

class EcoGestionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🌱 Sistema Gestión Ecológica Municipal")
        self.geometry("700x500")
        self.config(bg="#e8f5e9")

        self.pila = Pila()
        self.cola = Cola()
        self.lista = ListaEnlazada()
        self.arbol = ArbolBinarioBusqueda()
        self.grafo = Grafo()

        tk.Label(self, text="🌿 Gestión Ecológica Municipal", font=("Segoe UI", 18, "bold"), bg="#e8f5e9", fg="#2e7d32").pack(pady=20)

        opciones = [
            ("📚 Gestionar Historial (Pila)", self.gestionar_pila),
            ("📥 Gestionar Solicitudes (Cola)", self.gestionar_cola),
            ("📋 Gestionar Puntos y Áreas (Lista)", self.gestionar_lista),
            ("🌳 Gestionar Recursos Ecológicos (Árbol)", self.gestionar_arbol),
            ("🔗 Gestionar Relaciones (Grafo)", self.gestionar_grafo)
        ]

        for texto, comando in opciones:
            tk.Button(self, text=texto, font=("Segoe UI", 12), command=comando, bg="#a5d6a7", fg="black", width=40).pack(pady=5)

    def gestionar_pila(self):
        accion = simpledialog.askstring("Pila", "Escribe 'apilar' o 'desapilar':")
        if accion == "apilar":
            elemento = simpledialog.askstring("Apilar", "Introduce actividad:")
            self.pila.apilar(elemento)
        elif accion == "desapilar":
            if not self.pila.esta_vacia():
                elemento = self.pila.desapilar()
                messagebox.showinfo("Desapilado", f"Elemento '{elemento}' desapilado.")
            else:
                messagebox.showerror("Error", "La pila está vacía.")

    def gestionar_cola(self):
        accion = simpledialog.askstring("Cola", "Escribe 'encolar' o 'desencolar':")
        if accion == "encolar":
            elemento = simpledialog.askstring("Encolar", "Introduce solicitud:")
            self.cola.encolar(elemento)
        elif accion == "desencolar":
            if not self.cola.esta_vacia():
                elemento = self.cola.desencolar()
                messagebox.showinfo("Desencolado", f"Elemento '{elemento}' desencolado.")
            else:
                messagebox.showerror("Error", "La cola está vacía.")

    def gestionar_lista(self):
        accion = simpledialog.askstring("Lista", "Escribe 'insertar', 'eliminar' o 'consultar':")
        if accion == "insertar":
            elemento = simpledialog.askstring("Insertar", "Introduce punto o área:")
            self.lista.insertar(elemento)
        elif accion == "eliminar":
            elemento = simpledialog.askstring("Eliminar", "Introduce elemento a eliminar:")
            eliminado = self.lista.eliminar(elemento)
            if eliminado:
                messagebox.showinfo("Eliminado", f"Elemento '{elemento}' eliminado.")
            else:
                messagebox.showerror("Error", f"Elemento '{elemento}' no encontrado.")
        elif accion == "consultar":
            elementos = self.lista.recorrer()
            messagebox.showinfo("Lista", f"Elementos: {', '.join(elementos)}")

    def gestionar_arbol(self):
        accion = simpledialog.askstring("Árbol", "Escribe 'insertar' o 'buscar':")
        if accion == "insertar":
            elemento = simpledialog.askstring("Insertar", "Introduce recurso ecológico:")
            self.arbol.insertar(elemento)
        elif accion == "buscar":
            elemento = simpledialog.askstring("Buscar", "Introduce recurso a buscar:")
            existe = self.arbol.buscar(elemento)
            mensaje = "encontrado" if existe else "no encontrado"
            messagebox.showinfo("Búsqueda", f"Elemento '{elemento}' {mensaje}.")

    def gestionar_grafo(self):
        accion = simpledialog.askstring("Grafo", "Escribe 'conectar' o 'mostrar':")
        if accion == "conectar":
            origen = simpledialog.askstring("Origen", "Introduce origen:")
            destino = simpledialog.askstring("Destino", "Introduce destino:")
            self.grafo.agregar_arista(origen, destino)
        elif accion == "mostrar":
            inicio = simpledialog.askstring("Mostrar desde", "Introduce inicio:")
            recorrido = self.grafo.bfs(inicio)
            messagebox.showinfo("Grafo", f"Recorrido desde '{inicio}': {' ➡️ '.join(recorrido)}")

if __name__ == "__main__":
    app = EcoGestionApp()
    app.mainloop()