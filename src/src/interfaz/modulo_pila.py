import tkinter as tk
from pila import PilaActividades

pila = PilaActividades()

def mostrar_ventana_pila():
    ventana = tk.Toplevel()
    ventana.title("Actividades Ecológicas")
    ventana.geometry("400x300")
    ventana.configure(bg="#f0fff0")

    entrada = tk.Entry(ventana, width=30)
    entrada.pack(pady=5)

    efectividad = tk.Entry(ventana, width=30)
    efectividad.pack(pady=5)

    salida = tk.Text(ventana, height=10, width=45)
    salida.pack(pady=10)

    def agregar():
        actividad = entrada.get()
        try:
            nivel = int(efectividad.get())
            pila.agregar_actividad(actividad, nivel)
            salida.insert(tk.END, f"Agregada: {actividad} (Efectividad {nivel}/5)\n")
        except:
            salida.insert(tk.END, "Error: Efectividad debe ser entre 1 y 5.\n")
    

    def eliminar_ultima():
        actividad = pila.eliminar_ultima_actividad()
        if actividad:
            salida.insert(tk.END, f"Actividad eliminada: {actividad}\n")
        else:
            salida.insert(tk.END, "No hay actividades para eliminar.\n")

    tk.Button(ventana, text="Eliminar Última", command=eliminar_ultima, bg="#ccffcc").pack()



    def mostrar_todas():
        salida.delete(1.0, tk.END)
        if pila.esta_vacia():
            salida.insert(tk.END, "No hay actividades.\n")
        else:
            for i, (actividad, ef) in enumerate(reversed(pila.actividades), 1):
                salida.insert(tk.END, f"{i}. {actividad} (Efectividad: {ef}/5)\n")

    tk.Button(ventana, text="Agregar", command=agregar, bg="#ccffcc").pack()
    tk.Button(ventana, text="Mostrar Todas", command=mostrar_todas, bg="#ccffcc").pack()
