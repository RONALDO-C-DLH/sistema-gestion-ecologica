# Módulo de cola para gestionar las solicitudes de recolección especial segun la prioridad.

class ColaSolicitudes:
    def __init__(self):
        self.solicitudes = []



    # Se encarga de agrega una solicitud al sistema pero con un nivel de prioridad.
    def agregar_solicitud(self, solicitud, prioridad):
        self.solicitudes.append((prioridad, solicitud))
        self.solicitudes.sort(key=lambda x: x[0]) # Se ordena de manera tal que la más urgente quede de primero, es decir la que tenga el numero mas bajo.
        print(f"Solicitud agregada: {solicitud} (Prioridad: {prioridad})")
    


    # Atendera la solicitud con mayor prioridad
    def atender_solicitud(self):
        if self.esta_vacia():
            print("No hay solicitudes para atender.")
            return None
        
        prioridad, solicitud = self.solicitudes.pop(0)
        print(f"Solicitud atendida: {solicitud} (Prioridad: {prioridad})")
        return solicitud
    


    # Nos mostrara la siguiente solicitud en ser atendida.
    def ver_siguiente(self):
        if self.esta_vacia():
            print("No hay solicitudes en espera.")
            return None
        
        prioridad, solicitud = self.solicitudes[0]
        print(f"Próxima solicitud: {solicitud} (Prioridad: {prioridad})")
        return solicitud
    


    # Mantiendo el orden de prioridad mostrara todas las solicitudes que hacen falta.
    def mostrar_solicitudes(self):
        if self.esta_vacia():
            print("sin solicitudes.")
        else:
            print("Solicitudes pendientes (ordenadas por prioridad):")
            for i, (prioridad, solicitud) in enumerate(self.solicitudes, 1):
                print(f"{i}. {solicitud} (Prioridad: {prioridad})")
    



    # verificara que no haya solicitudes faltantes, osea que este vacia.
    def esta_vacia(self):
        return len(self.solicitudes) == 0
    
