"""Modulo que centraliza a função de extrair o relatorio do site da total cash, juntando todos os submodulos ligados a essa ação"""
# Faça as importações aqui.... (Com execeção de outros modulos e recursos propircios a erro de importação circular, esses você deve importar dentro do escopo da classe/metodo/função)

from utils.imports import *

def example(): 

    # Importação de submodulos e recursos necessários
    from utils import error, sucess, info_module # Modulos de saídas de prints padronizadas

    # Obtem o nome do arquivo atual e passa para o metodo de imprimir o nome do modulo atual
    info_module(str(os.path.basename(__file__)))

    try:
        
        teste = 'Thiago'
        
        # Retorna uma saída de print de sucesso padronizada
        sucess(teste)

    except Exception as E:

        # Retorna uma saída de print de erro padronizada
        error(f"Não foi possível extrair o relatorio base\nERRO: {E}")