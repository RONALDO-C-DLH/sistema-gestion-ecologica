import tkinter as tk
from arbol import RecursoEcologico, ArbolRecursos

arbol = ArbolRecursos()

def mostrar_ventana_arbol():
    ventana = tk.Toplevel()
    ventana.title("Recursos Ecológicos")
    ventana.geometry("400x300")
    ventana.configure(bg="#f0f8ff")

    tipo = tk.Entry(ventana, width=30)
    tipo.insert(0, "Tipo")
    tipo.pack(pady=2)

    nombre = tk.Entry(ventana, width=30)
    nombre.insert(0, "Nombre")
    nombre.pack(pady=2)

    ubicacion = tk.Entry(ventana, width=30)
    ubicacion.insert(0, "Ubicación")
    ubicacion.pack(pady=2)

    salida = tk.Text(ventana, height=10, width=45)
    salida.pack()
    

    busqueda = tk.Entry(ventana, width=30)
    busqueda.insert(0, "Buscar por nombre")
    busqueda.pack(pady=2)

    def buscar():
        r = arbol.buscar_por_nombre(busqueda.get())
        salida.delete(1.0, tk.END)
        if r:
            salida.insert(tk.END, f"Encontrado: {r.nombre} - {r.tipo} - {r.ubicacion}\n")
                          
        else:
            salida.insert(tk.END, "No se encontró el recurso \n")

    tk.Button(ventana, text="Buscar", command=buscar, bg="#cce6ff").pack()


    def agregar():
        recurso = RecursoEcologico(tipo.get(), nombre.get(), ubicacion.get())
        arbol.insertar(recurso)
        salida.insert(tk.END, "Recurso agregado\n")

    def mostrar():
        salida.delete(1.0, tk.END)
        def imprimir(nodo):
            if nodo:
                imprimir(nodo.izquierda)
                r = nodo.recurso
                salida.insert(tk.END, f"{r.nombre} - {r.tipo} - {r.ubicacion}\n")
                imprimir(nodo.derecha)
        imprimir(arbol.raiz)

    tk.Button(ventana, text="Agregar", command=agregar, bg="#cce6ff").pack()
    tk.Button(ventana, text="Mostrar En Orden", command=mostrar, bg="#cce6ff").pack()