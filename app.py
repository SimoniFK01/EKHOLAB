from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from supabase import create_client, Client
import os

app = Flask(__name__)
CORS(app)

# Configurações do Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://xuvjvmysjudwgkkjelca.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Rota Principal (Renderiza a Tela Inicial)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
