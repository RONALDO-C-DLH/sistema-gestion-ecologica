import tkinter as tk
from lista import ListaEnlazada

lista = ListaEnlazada()

def mostrar_ventana_lista():
    ventana = tk.Toplevel()
    ventana.title("Elementos Ecológicos")
    ventana.geometry("400x300")
    ventana.configure(bg="#f9e6ff")

    entrada = tk.Entry(ventana, width=30)
    entrada.pack(pady=5)

    salida = tk.Text(ventana, height=10, width=45)
    salida.pack()

    def insertar():
        lista.insertar(entrada.get())
        salida.insert(tk.END, "Elemento insertado\n")

    def mostrar():
        salida.delete(1.0, tk.END)
        for dato in lista.recorrer():
            salida.insert(tk.END, f"{dato}\n")

    tk.Button(ventana, text="Insertar", command=insertar, bg="#ffccff").pack()
    tk.Button(ventana, text="Mostrar Lista", command=mostrar, bg="#ffccff").pack()
