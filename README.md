# Web Deutsch

Aplicación web para practicar la traducción de vocabulario y frases entre inglés y alemán, construida con Flask.

## Requisitos
- Python 3.9+

## Instalación

1. Clona el repositorio.
2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

## Ejecución

1. Inicia la aplicación:
   ```bash
   python app.py
   ```
2. Abre tu navegador en `http://127.0.0.1:5000`.

## Estructura del Proyecto
- `app.py`: Configuración inicial y punto de entrada de la aplicación.
- `routes.py`: Definición de rutas y controladores HTTP.
- `game_logic.py`: Funciones de lógica auxiliar y carga de datos.
- `data/`: Directorio que contiene los archivos de vocabulario (`.csv`, `.xlsx`).
- `templates/`: Plantillas HTML para el renderizado web.
