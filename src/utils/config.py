from utils.imports import *
# src/utils/config.py

load_dotenv()

# Raiz do projeto (root/)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ===============================
# API KEYS
# ===============================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "A chave da API Gemini não está definida. "
        "Defina a variável de ambiente 'GEMINI_API_KEY'."
    )

# ===============================
# FILE PATHS
# ===============================
SITES_FILE_PATH_ENV = os.getenv("SITES_FILE_PATH")

if not SITES_FILE_PATH_ENV:
    raise ValueError(
        "A variável de ambiente 'SITES_FILE_PATH' não está definida."
    )

SITES_FILE_PATH = BASE_DIR / SITES_FILE_PATH_ENV

if not SITES_FILE_PATH.exists():
    raise FileNotFoundError(
        f"Arquivo de sites não encontrado em: {SITES_FILE_PATH}"
    )
