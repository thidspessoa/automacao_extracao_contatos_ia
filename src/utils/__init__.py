import sys
import os

# Configura o pythonpath no sistema para procurar pelos pacotes a partir da raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# importa todos os modulos do pacote utils
from utils.config import *
from utils.utils_functions import *
from utils.imports import *
from utils.abstract_class import Shape