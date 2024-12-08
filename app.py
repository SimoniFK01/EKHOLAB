from flask import Flask
from supabase import create_client, Client
import os

app = Flask(__name__)

# Configuração do Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://xuvjvmysjudwgkkjelca.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Teste de Conexão
@app.route('/')
def index():
    try:
        # Apenas teste de conexão ao Supabase
        response = supabase.table("itens_romaneio").select("*").limit(1).execute()
        return "Conexão bem-sucedida com Supabase!", 200
    except Exception as e:
        return f"Erro ao conectar ao Supabase: {str(e)}", 500

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
