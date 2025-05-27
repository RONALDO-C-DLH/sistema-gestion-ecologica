import tkinter as tk
from cola import ColaSolicitudes

cola = ColaSolicitudes()

def mostrar_ventana_cola():
    ventana = tk.Toplevel()
    ventana.title("Solicitudes")
    ventana.geometry("400x300")
    ventana.configure(bg="#fff0f0")

    entrada = tk.Entry(ventana, width=30)
    entrada.pack(pady=5)

    prioridad = tk.Entry(ventana, width=30)
    prioridad.pack(pady=5)

    salida = tk.Text(ventana, height=10, width=45)
    salida.pack(pady=10)

    def agregar():
        try:
            cola.agregar_solicitud(entrada.get(), int(prioridad.get()))
            salida.insert(tk.END, "Solicitud agregada\n")
        except:
            salida.insert(tk.END, "Error en la prioridad\n")

    def mostrar():
        salida.delete(1.0, tk.END)
        for i, (p, s) in enumerate(cola.solicitudes, 1):
            salida.insert(tk.END, f"{i}. {s} (Prioridad: {p})\n")

    tk.Button(ventana, text="Agregar", command=agregar, bg="#ffcccc").pack()
    tk.Button(ventana, text="Mostrar Todas", command=mostrar, bg="#ffcccc").pack()
