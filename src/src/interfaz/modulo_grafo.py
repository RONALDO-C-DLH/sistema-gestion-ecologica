import tkinter as tk
from grafo import GrafoIniciativas

grafo = GrafoIniciativas()

def mostrar_ventana_grafo():
    ventana = tk.Toplevel()
    ventana.title("Iniciativas Ecológicas")
    ventana.geometry("400x300")
    ventana.configure(bg="#fffbe6")

    nombre = tk.Entry(ventana, width=30)
    nombre.pack(pady=5)

    conexion = tk.Entry(ventana, width=30)
    conexion.pack(pady=5)

    salida = tk.Text(ventana, height=10, width=45)
    salida.pack()

    def agregar():
        grafo.agregar_iniciativa(nombre.get())
        salida.insert(tk.END, "Iniciativa agregada\n")

    def conectar():
        grafo.conectar_iniciativas(nombre.get(), conexion.get())
        salida.insert(tk.END, "Conexión realizada\n")

    def mostrar():
        salida.delete(1.0, tk.END)
        for nodo, vecinos in grafo.grafo.items():
            salida.insert(tk.END, f"{nodo} -> {', '.join(vecinos)}\n")

    tk.Button(ventana, text="Agregar", command=agregar, bg="#ffffcc").pack()
    tk.Button(ventana, text="Conectar", command=conectar, bg="#ffffcc").pack()
    tk.Button(ventana, text="Mostrar", command=mostrar, bg="#ffffcc").pack()
