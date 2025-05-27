# app.py
import threading
import tkinter as tk
from tkinter import ttk, messagebox

# Importa tus funciones aquí. Ajusta los nombres si difieren.
from cli import cargar_lista, cargar_cola, cargar_arbol, cargar_grafo
from main import main as ejecutar_main

class EcoGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión Ecológica Municipal")
        self.geometry("700x500")
        self._build_ui()

    def _build_ui(self):
        header = ttk.Frame(self, padding=10)
        header.pack(fill="x")

        ttk.Label(header, text="🌿 Gestión Ecológica", font=("Segoe UI", 18, "bold")).pack(side="left")

        btns = ttk.Frame(header)
        btns.pack(side="right")
        for (txt, cmd) in [
            ("Cargar Lista", self._run_threaded, cargar_lista),
            ("Cargar Cola", self._run_threaded, cargar_cola),
            ("Cargar Árbol", self._run_threaded, cargar_arbol),
            ("Cargar Grafo", self._run_threaded, cargar_grafo),
            ("Ejecutar Main", self._run_threaded, ejecutar_main),
        ]:
            b = ttk.Button(btns, text=txt, command=lambda c=cmd: self._run_threaded(c))
            b.pack(side="left", padx=5)

        # Text area para mostrar resultados
        self.log = tk.Text(self, wrap="word", state="disabled")
        self.log.pack(fill="both", expand=True, padx=10, pady=10)

        footer = ttk.Frame(self, padding=5)
        footer.pack(fill="x")
        ttk.Label(footer, text="© 2025 Gestión Ecológica Municipal · info@eco.com",
                  font=("Segoe UI", 9)).pack(side="right")

    def _run_threaded(self, func):
        """Ejecuta la función en segundo plano para no bloquear la UI."""
        threading.Thread(target=self._execute, args=(func,), daemon=True).start()

    def _execute(self, func):
        """Llama a la función, captura su retorno o excepción y lo muestra."""
        self._append(f"⏳ Ejecutando {func.__name__} …\n")
        try:
            result = func()
            self._append(f"✔ {func.__name__} completado.\n")
            self._append("Salida:\n")
            self._append(f"{result}\n\n")
        except Exception as e:
            self._append(f"❌ Error en {func.__name__}: {e}\n\n")

    def _append(self, text):
        """Inserta texto en el log de manera thread-safe."""
        def inner():
            self.log.configure(state="normal")
            self.log.insert("end", text)
            self.log.see("end")
            self.log.configure(state="disabled")
        self.after(0, inner)

if __name__ == "__main__":
    app = EcoGUI()
    app.mainloop()
