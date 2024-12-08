from flask import Flask, render_template, request, jsonify
import requests
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

SUPABASE_URL = app.config['SUPABASE_URL']
SUPABASE_KEY = app.config['SUPABASE_KEY']

# Cabeçalhos para autenticação na API do Supabase
headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

@app.route('/')
def index():
    return "Hello, Flask no Render!"
    
# Exemplo de busca no Supabase
@app.route('/get_data', methods=['GET'])
def get_data():
    table_name = "sua_tabela"  # Substitua pelo nome da sua tabela
    response = requests.get(f"{SUPABASE_URL}/rest/v1/{table_name}", headers=headers)
    data = response.json()
    return jsonify(data)

# Exemplo de inserção no Supabase
@app.route('/add_data', methods=['POST'])
def add_data():
    table_name = "sua_tabela"  # Substitua pelo nome da sua tabela
    payload = request.json
    response = requests.post(f"{SUPABASE_URL}/rest/v1/{table_name}", headers=headers, json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

