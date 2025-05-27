from tkinter import Tk, Button, Label
from interfaz.modulo_pila import mostrar_ventana_pila
from interfaz.modulo_cola import mostrar_ventana_cola
from interfaz.modulo_arbol import mostrar_ventana_arbol
from interfaz.modulo_grafo import mostrar_ventana_grafo
from interfaz.modulo_lista import mostrar_ventana_lista

class VentanaPrincipal:
    def __init__(self, master):
        master.title("Gestor Ecológico Municipal")
        master.geometry("500x400")
        master.configure(bg="#e6ffe6")

        Label(master, text="GESTOR ECOLÓGICO", font=("Arial", 20, "bold"), bg="#e6ffe6", fg="green").pack(pady=20)

        botones = [
            ("Actividades (Pila)", mostrar_ventana_pila),
            ("Solicitudes (Cola)", mostrar_ventana_cola),
            ("Recursos (Árbol)", mostrar_ventana_arbol),
            ("Iniciativas (Grafo)", mostrar_ventana_grafo),
            ("Elementos (Lista)", mostrar_ventana_lista)
        ]

        for texto, comando in botones:
            Button(master, text=texto, command=cmd(comando), width=30, height=2, bg="#b3ffb3", fg="black").pack(pady=5)

def cmd(f):  # Evita problemas con la lambda y referencias tardías
    return lambda: f()
