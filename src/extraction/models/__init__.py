import sys
import os

# Configura o pythonpath no sistema para procurar pelos pacotes a partir da raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importe seus modulos abaixo....
# from models.load_jsons import credentials, xpaths, directories
# from models.requests_api import *