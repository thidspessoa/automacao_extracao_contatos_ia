import sys
import os

# Configura o pythonpath no sistema para procurar pelos pacotes a partir da raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Importe seus modulos abaixo...
from extraction.controllers import *
from extraction.services import *
from extraction.models import *