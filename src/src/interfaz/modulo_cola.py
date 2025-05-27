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

    
    def atender():
        solicitud = cola.atender_solicitud()
        if solicitud:
            salida.insert(tk.END, f"Atendida: {solicitud}\n")
        else:
            salida.insert(tk.END, "No hay solicitudes para atender.\n")

    def siguiente():
        solicitud = cola.ver_siguiente()
        if solicitud:
            salida.insert(tk.END, f"Siguiente: {solicitud}\n")
        else:
            salida.insert(tk.END, "No hay solicitudes pendientes.\n")

    tk.Button(ventana, text="Atender Solicitud", command=atender, bg="#ffcccc").pack()
    tk.Button(ventana, text="Ver Siguiente", command=siguiente, bg="#ffcccc").pack()


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
