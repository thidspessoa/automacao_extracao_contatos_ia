# Importa diretamente do arquivo de configuração, todas as depedencias do projeto
from src.utils.imports import *

# Configura o path do python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def main():

    # Importação de modulos
    from utils import ChromeDriver, ColorManager
    from extraction.controllers.instagram import InstagramExtractor
    
    # Caminho para o arquivo que será lido
    from utils.config import SITES_FILE_PATH


    # Cria uma instancia da classe de gerenciamento do navegador
    webdriver = ChromeDriver()

    # Instância de referencia do chromedriver
    browser = webdriver.browser

    try:
        
        ColorManager.info('Iniciando a automação...')
    
        # Abre o arquivo sites.txt e le os links
        with open(SITES_FILE_PATH, 'r') as file:
                        
            # Itera sobre cada linha do arquivo, cada link
            for line in file.readlines():
                
                site = line.strip()
                
                if not site: # Se a linha do arquivo for vazia
                    continue  # Pula linhas vazias
                
                ColorManager.warning(f'Processando site: {site}')
                
                # Verifica se o site é do instagram
                if "instagram.com" in site:
                    
                    continue # Stand-by para evitar execuções acidentais, pois vou desenvolver esse módulo ainda posteriormente
                    
                    ColorManager.info('Iniciando extração de dados do Instagram...')
                    
                    # Cria uma instancia do extrator de instagram
                    instagram_extractor: InstagramExtractor = InstagramExtractor(browser, site)
                    instagram_extractor.extract_profile_data() # Metodo para extrair os dados do perfil
            
                    # # Executa a extração de contatos
                    # instagram_extractor.extract_contacts()
                    
                # Se for a landing page da empresa
                else:
                    
                    ColorManager.info('Iniciando extração de dados da landing page...')
                    
                    
                    

        
        # Chama o modulo de tratamento do html e extração dos contatos usando IA
        # Chama o modulo de disparo de mensagens no wpp

        # Se o código chegar até aqui sem exceções, a execução foi bem-sucedida
        execution_successful = True

    except Exception as e:

        # Retorna uma saída de print de erro padronizada
        ColorManager.error(f'Erro na automação: {e}')

        # Encerra a instância do wedriver aberta
        webdriver.kill_browser()

    finally:

        # Se a execução tiver ocorrido normalmente, envia o email de sucesso
        if execution_successful:

            # Retorna uma saída de print de sucesso padronizada
            ColorManager.success('Automação concluída com sucesso.')

        # Finaliza o navegador utilizando o metodo kill browser
        webdriver.kill_browser()


if __name__ == "__main__":
    main()
