import tkinter as tk
from tareas import GestorTareas

gestor = GestorTareas()


def mostrar_ventana_tareas():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Tareas")
    ventana.geometry("400x300")
    ventana.configure(bg="#e6e6ff")

    entrada = tk.Entry(ventana, width=30)
    entrada.pack(pady=5)

    indice = tk.Entry(ventana, width=30)
    indice.pack(pady=5)

    salida = tk.Text(ventana, height=10, width=45)
    salida.pack(pady=10)

    def agregar():
        gestor.agregar_tarea(entrada.get())
        salida.insert(tk.END, "Tarea agregada\n")

    def completar():
        try:
            pos = int(indice.get()) - 1
            if gestor.completar_tarea(pos):
                salida.insert(tk.END, "Tarea completada\n")
            else:
                salida.insert(tk.END, "Índice fuera de rango\n")
        except Exception:
            salida.insert(tk.END, "Índice inválido\n")

    def mostrar():
        salida.delete(1.0, tk.END)
        for i, tarea in enumerate(gestor.obtener_tareas(), 1):
            estado = "✓" if tarea["completada"] else "✗"
            salida.insert(tk.END, f"{i}. {tarea['descripcion']} [{estado}]\n")

    tk.Button(ventana, text="Agregar", command=agregar, bg="#ccccff").pack()
    tk.Button(ventana, text="Completar", command=completar, bg="#ccccff").pack()
    tk.Button(ventana, text="Mostrar Todas", command=mostrar, bg="#ccccff").pack()
