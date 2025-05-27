import tkinter as tk
from lista import ListaEnlazada

lista = ListaEnlazada()

def mostrar_ventana_lista():
    ventana = tk.Toplevel()
    ventana.title("Zonas Verdes")
    ventana.geometry("400x300")
    ventana.configure(bg="#f9e6ff")

    entrada = tk.Entry(ventana, width=30)
    entrada.pack(pady=5)

    salida = tk.Text(ventana, height=10, width=45)
    salida.pack()

    
    def buscar():
        existe = lista.buscar(entrada.get())
        if existe:
            salida.insert(tk.END, f"Zona Verde encontrada: {entrada.get()}\n")
        else:
            salida.insert(tk.END, f"No se encontró: {entrada.get()}\n")

    def eliminar():
        eliminado = lista.eliminar(entrada.get())
        if eliminado:
            salida.insert(tk.END, f"Zona eliminado: {entrada.get()}\n")
        else:
            salida.insert(tk.END, f"No se pudo eliminar: {entrada.get()}\n")

    tk.Button(ventana, text="Buscar", command=buscar, bg="#ffccff").pack()
    tk.Button(ventana, text="Eliminar", command=eliminar, bg="#ffccff").pack()


    def insertar():
        lista.insertar(entrada.get())
        salida.insert(tk.END, "Zona Verde Ingresada\n")

    def mostrar():
        salida.delete(1.0, tk.END)
        for dato in lista.recorrer():
            salida.insert(tk.END, f"{dato}\n")

    tk.Button(ventana, text="Insertar", command=insertar, bg="#ffccff").pack()
    tk.Button(ventana, text="Mostrar Lista", command=mostrar, bg="#ffccff").pack()
