# Sistema de Gestión Ecológica Municipal

## Descripción
Aplicación para gestionar recursos ecológicos en la ciudad:
- **Pilas:** Historial de campañas.
- **Colas:** Solicitudes de recogida especial.
- **Listas:** Puntos limpios y áreas verdes.
- **Árboles:** Búsqueda geográfica o por tipo.
- **Grafos:** Relaciones entre iniciativas comunitarias.

## Tecnologías
- Python 3.x
- Estructuras de datos propias

## Instalación
1. `git clone <url-del-repo>`
2. `cd sistema-gestion-ecologica`
3. (Opcional) crear ambiente virtual: `python -m venv venv`  
4. Instalar dependencias: `pip install -r requirements.txt`

## Uso
```bash
python src/main.py

## 📚 Documentación

La documentación automática está en:  
https://<tu-usuario>.github.io/sistema-gestion-ecologica/

Para generarla localmente:

```bash
# Activa el entorno
source venv/Scripts/activate  
# Genera los .rst
python -m sphinx.ext.apidoc -o docs src  
# Compila los HTML
cd docs
make.bat html

