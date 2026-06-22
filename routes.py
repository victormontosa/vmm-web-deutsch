from flask import request, session, redirect, url_for, render_template
from game_logic import cargar_frases_desde_csv
from app import app
import os

# Ruta al directorio donde se encuentran los archivos de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_data = os.path.join(BASE_DIR, "data")

@app.route("/", methods=["GET", "POST"])
def index():
    if 'idioma' not in session:
        session['idioma'] = 'EN_DE'  # Dirección de traducción predeterminada: Inglés a Alemán
    if request.method == "POST":
        frases_origen, frases_destino = (session['frases_en'], session['frases_de']) if session['idioma'] == 'EN_DE' else (session['frases_de'], session['frases_en'])
        frase_origen = request.form["frase_origen"]
        traduccion_usuario = request.form["traduccion"]
        indice_correcto = frases_origen.index(frase_origen)
        traduccion_correcta = frases_destino[indice_correcto]

        # Verifica si la respuesta del usuario es correcta
        if traduccion_usuario == traduccion_correcta:
            resultado = "¡Correcto!"
            session['racha'] += 1  # Incrementa la racha

            # Actualiza el récord de racha si la racha actual es mayor
            if 'record_racha' not in session or session['racha'] > session.get('record_racha', 0):
                session['record_racha'] = session['racha']

        else:
            resultado = f"Incorrecto. La traducción correcta era: '{traduccion_correcta}'"
            session['racha'] = 0  # Restablece la racha a 0 si la respuesta es incorrecta

            # Añade la frase y su traducción correcta a los recordatorios
            if 'recordatorios' not in session:
                session['recordatorios'] = []
            session['recordatorios'].append(f"{frase_origen} - {traduccion_correcta}")
        
        # Asegúrate de marcar la sesión como modificada para guardar los cambios
        session.modified = True

        # Renderiza la página con el resultado, la racha actual, el récord de racha, y los recordatorios actualizados
        return render_template('web.html', resultado=resultado, juego_iniciado=True, idioma=session['idioma'])
    else:
    # Aquí continuaría el resto de la lógica para manejar peticiones GET, como iniciar el juego

        # Si no es una solicitud POST, carga las frases y comienza el juego normalmente
        session['frases_en'], session['frases_de'] = cargar_frases_desde_csv(os.path.join(path_data, 'frases.csv'))
        if 'racha' not in session:
            session['racha'] = 0  # Asegúrate de que la racha se inicializa al comenzar
        return iniciar_juego()

@app.route("/cambiar_idioma")
def cambiar_idioma():
    session['idioma'] = 'DE_EN' if session['idioma'] == 'EN_DE' else 'EN_DE'
    return redirect(url_for('index'))

from flask import render_template
import random

def iniciar_juego():
    if 'racha' not in session:
        session['racha'] = 0 
    frases_origen, frases_destino = (session['frases_en'], session['frases_de']) if session['idioma'] == 'EN_DE' else (session['frases_de'], session['frases_en'])
    indice_correcto = random.randint(0, len(frases_origen) - 1)
    opciones = [frases_destino[indice_correcto]]
    while len(opciones) < 4:
        opcion = random.choice(frases_destino)
        if opcion not in opciones:
            opciones.append(opcion)
    random.shuffle(opciones)
    frase_origen = frases_origen[indice_correcto]
    return render_template('web.html', opciones=opciones, frase_origen=frase_origen, juego_iniciado=False, idioma=session['idioma'])

