import os

class Config:
    SUPABASE_URL = os.getenv("SUPABASE_URL", "https://xuvjvmysjudwgkkjelca.supabase.co")  # URL do Supabase
    SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5...")  # Substitua pela sua API Key
