"""Classe abstrata para definir o padrão para todas as demais classes utilitarias"""

from abc import ABC, abstractmethod
from utils.utils_functions.color_manager import ColorManager
from utils.imports import *

class Shape(ABC):
    """Classe abstrata para definir um padrão para as demais.
    
    Methods:
        info_method(self)
    """    

    @abstractmethod
    def __init__(self):
        """Construtor que obtém automaticamente o nome do arquivo."""
        # PASSO 1: Obtém o frame (contexto) da classe que chamou
        frame = inspect.currentframe().f_back
        
        # PASSO 2: Acessa as variáveis globais do frame
        globals_dict = frame.f_globals
        
        # PASSO 3: Obtém o caminho do arquivo
        class_file = globals_dict.get('__file__', 'desconhecido.py')
        
        # PASSO 4: Extrai apenas o nome do arquivo (sem caminho)
        self.file_name = os.path.basename(class_file)

    def info_method(self, method_name):
        
        ColorManager.info(f'File: {self.file_name} | Class: {self.__class__.__name__} | Method: {method_name}')