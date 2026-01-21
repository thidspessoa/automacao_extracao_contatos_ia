import os
import sys

# Configura o pythonpath no sistema para procurar pelos pacotes a partir da raiz do projeto
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '...'))
)


# Importa os modulos dessa pasta
from utils.utils_functions.browser_utils import BrowserActions, BrowserUtils
from utils.utils_functions.file_utils import MoveFiles, SaveDeleteFiles
from utils.utils_functions.whatsapp_utils import WhatsappFileUtils
from utils.utils_functions.color_manager import ColorManager
from utils.utils_functions.init_browser import ChromeDriver