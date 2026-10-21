from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/consultar', methods=['POST'])
def consultar_recetas():
    datos = request.json
    ingreso_usuario = datos.get('ingrediente', 'tortillas_de_harina')
    
    # Ruta de tu archivo recetas.pl (asegúrate de que esté en la misma carpeta)
    ruta_prolog = os.path.join(os.getcwd(), 'recetas.pl')
    
    # Consulta que le mandaremos a Prolog (ejemplo: nuestra Regla 2)
    # Le preguntamos qué receta usa el ingrediente que ingresó el usuario
    consulta = f"recomendar_receta(Receta, {ingreso_usuario})."
    
    try:
        # Comando para ejecutar SWI-Prolog desde la consola de forma silenciosa
        # (Asegúrate de que 'swipl' esté reconocido en el sistema)
        comando = ['swipl', '-s', ruta_prolog, '-g', f"{consulta}, writeln(Receta), fail;", '-t', 'halt']
        
        resultado = subprocess.run(comando, capture_output=True, text=True, timeout=5)
        
        # Capturamos la salida que genera Prolog
        salida_prolog = resultado.stdout.strip()
        
        # Procesamos las respuestas obtenidas
        recetas_encontradas = [r.strip() for r in salida_prolog.split('\n') if r.strip()]
        
        return jsonify({
            "exito": True, 
            "motor": "SWI-Prolog Real",
            "recomendaciones": recetas_encontradas
        })
        
    except Exception as e:
        return jsonify({
            "exito": False, 
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)