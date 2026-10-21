from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

MAPEO_INGREDIENTES = {
    'pollo_asado': ['pollo_deshebrado', 'pollo_asado'],
    'pollo_rostizado': ['pollo_deshebrado', 'pollo_rostizado'],
    'pollo_deshebrado': ['pollo_deshebrado'],
    'tortillas_de_maiz': ['tortillas_de_harina', 'tortillas_de_maiz'],
    'tortillas_de_harina': ['tortillas_de_harina'],
    'queso_panela': ['quesillo_deshebrado', 'queso_panela'],
    'queso_gouda': ['quesillo_deshebrado', 'queso_gouda'],
    'queso_asadero': ['quesillo_deshebrado', 'queso_asadero'],
    'quesillo_deshebrado': ['quesillo_deshebrado'],
    'caja_de_caldillo_de_tomate': ['dos_jitomates', 'caja_de_caldillo_de_tomate'],
    'dos_jitomates': ['dos_jitomates']
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/consultar', methods=['POST'])
def consultar_recetas():
    datos = request.json
    ingredientes_usuario = datos.get('ingredientes', [])
    
    ruta_prolog = os.path.join(os.getcwd(), 'recetas.pl')
    recetas_encontradas = set()
    
    try:
        ingredientes_a_consultar = set()
        for ing in ingredientes_usuario:
            if ing in MAPEO_INGREDIENTES:
                ingredientes_a_consultar.update(MAPEO_INGREDIENTES[ing])
            else:
                ingredientes_a_consultar.add(ing)

        for ing in ingredientes_a_consultar:
            # Quitamos el punto interno para que la sintaxis de SWI-Prolog sea correcta
            consulta = f"recomendar_receta(Receta, {ing})"
            
            comando = ['swipl', '-s', ruta_prolog, '-g', f"{consulta}, writeln(Receta), fail", '-t', 'halt']
            
            resultado = subprocess.run(comando, capture_output=True, text=True, timeout=5)
            
            salida = resultado.stdout.strip()
            if salida:
                for r in salida.split('\n'):
                    if r.strip():
                        recetas_encontradas.add(r.strip())
        
        return jsonify({
            "exito": True, 
            "motor": "SWI-Prolog Real",
            "recomendaciones": list(recetas_encontradas)
        })
        
    except Exception as e:
        return jsonify({
            "exito": False, 
            "error": str(e),
            "recomendaciones": []
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)