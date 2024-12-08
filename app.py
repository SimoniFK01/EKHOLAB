from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import psycopg2
from psycopg2.extras import DictCursor
import os

app = Flask(__name__)
CORS(app)

# Configurações do Banco de Dados
db_config = {
    "host": "aws-0-sa-east-1.pooler.supabase.com",
    "user": "postgres",
    "password": "Ff456123!",  # Substitua por sua senha
    "database": "postgres",
    "port": 6543
}

# Testar a Conexão com o Banco de Dados
def test_db_connection():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("SELECT 1;")  # Consulta simples para testar
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] == 1
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False

# Rota Principal (Renderiza a Tela Inicial)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para Testar Conexão com o Banco de Dados
@app.route('/test-db', methods=['GET'])
def test_db():
    if test_db_connection():
        return jsonify({"status": "success", "message": "Conexão com o banco de dados bem-sucedida!"}), 200
    else:
        return jsonify({"status": "error", "message": "Erro ao conectar ao banco de dados."}), 500

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
