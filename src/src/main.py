from tkinter import Tk
from interfaz.ventana_principal import VentanaPrincipal

def main():
    root = Tk()
    app = VentanaPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
