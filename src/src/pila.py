# Módulo para la gestión del Historial reciente sobre actividades ecológicas realizadas (por ejemplo, campañas),
# permitiendo evaluar qué iniciativas han sido más efectivas.

class PilaActividades:
    def __init__(self):
        self.actividades = []



    # Se encarga de agregar una actividad ecológica unto con su nivel de efectividad (1 al 5).
    def agregar_actividad(self, actividad, efectividad):
        self.actividades.append((actividad, efectividad))
        print(f"Actividad agregada: {actividad} (Efectividad: {efectividad}/5)")



    # Nos muestra la última actividad que fue agregada pero sin eliminar esta.
    def ver_ultima_actividad(self):
        if self.esta_vacia():
            print("No hay actividades registradas.")
            return None
        
        actividad, efectividad = self.actividades[-1]
        print(f"Última actividad: {actividad} (Efectividad: {efectividad}/5)")
        return actividad
    


    # Eliminara la última actividad registrada osea, la más reciente.
    def eliminar_ultima_actividad(self):
        if self.esta_vacia():
            print("No hay actividades para eliminar.")
            return None
        
        actividad, efectividad = self.actividades.pop()
        print(f"Actividad eliminada: {actividad} (Efectividad: {efectividad}/5)")
        return actividad
    


    # Esta mostrara todas las actividades que se han registrado hasta el momento.
    def mostrar_actividades(self):
        if self.esta_vacia():
            print("La pila está vacía.")

        else:
            print("Historial de actividades ecológicas:")
            for i, (actividad, efectividad) in enumerate(reversed(self.actividades), 1):
                print(f"{i}. {actividad} (Efectividad: {efectividad}/5)")



    # Ya esta Verifica si no hay ninguna actividad.
    def esta_vacia(self):
        return len(self.actividades) == 0
