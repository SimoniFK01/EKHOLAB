from flask import Flask, request, jsonify, render_template
import pymysql
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Permite requisições de outros domínios (Cross-Origin Resource Sharing)

# Configurações do Banco de Dados
db_config = {
    "host": os.getenv("DB_HOST", "aws-0-sa-east-1.pooler.supabase.com"),
    "user": os.getenv("DB_USER", "postgres.hotzezvnfvepcmgbybkj"),
    "password": os.getenv("DB_PASSWORD", "Ff456123!"),
    "database": os.getenv("DB_NAME", "postgres")
}

# Rota Principal (Renderiza a Tela Inicial)
@app.route('/')
def index():
    return render_template('index.html')  # Serve o arquivo index.html


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
