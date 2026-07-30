import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "podcast_config.json")

def load_config():
    """Carrega as configurações personalizadas do arquivo podcast_config.json"""
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[!] Erro ao ler {CONFIG_PATH}: {e}. Usando padrões.")
            
    # Configuração fallback padrão se o arquivo não existir
    return {
        "podcast": {
            "title": "Meu Podcast de TI",
            "tagline": "Tudo sobre Programação & IA Descomplicada",
            "description": "Podcast diário sobre tecnologia e desenvolvimento.",
            "author": "Apresentadores do Podcast",
            "email": "contato@exemplo.com",
            "link": "https://seu-usuario.github.io/seu-repositorio",
            "category": "Technology",
            "language": "pt-br",
            "schedule_time_brt": "07:00 da manhã"
        },
        "hosts": {
            "host_1": {
                "name": "Tico",
                "voice": "pt-BR-AntonioNeural",
                "role": "O estudante curioso de tecnologia."
            },
            "host_2": {
                "name": "Tech",
                "voice": "pt-BR-FranciscaNeural",
                "role": "A especialista e tutora de dados."
            },
            "mascot": {
                "name": "Robô de IA",
                "role": "Assistente virtual."
            }
        },
        "feeds": [
            {"name": "freeCodeCamp PT", "url": "https://www.freecodecamp.org/portuguese/news/rss/"},
            {"name": "Blog Alura", "url": "https://www.alura.com.br/artigos/rss"},
            {"name": "TabNews", "url": "https://www.tabnews.com.br/rss"}
        ],
        "keywords": ["python", "sql", "programação", "tecnologia", "desenvolvimento", "ia", "dados"]
    }
