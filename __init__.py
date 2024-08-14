from flask import Flask

# Inicializar la aplicación Flask
app = Flask(__name__)

# Importar las rutas (esto se hace después de crear la app para evitar dependencias circulares)
from app import routes
