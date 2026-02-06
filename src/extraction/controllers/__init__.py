import sys
import os

# Configura o pythonpath no sistema para procurar pelos pacotes a partir da raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Importe seus modulos abaixo...
from src.extraction.controllers.website import WebSiteExtractor
from src.extraction.controllers.instagram import InstagramExtractor