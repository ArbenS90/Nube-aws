from flask import Flask

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Definimos una ruta para la página principal
@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

# Este bloque asegura que el servidor solo se ejecute cuando
# el script se ejecute directamente desde Python, y no cuando
# se importe desde otro script.
if __name__ == '__main__':
    # Ejecutamos la aplicación Flask en modo de desarrollo
    app.run(debug=True)
