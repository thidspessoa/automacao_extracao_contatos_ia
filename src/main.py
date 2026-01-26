# Importa diretamente do arquivo de configuração, todas as depedencias do projeto
from src.utils.imports import *

# Configura o path do python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def main():

    # Importação de modulos
    from utils import ChromeDriver, ColorManager
    from extraction.controllers.instagram import InstagramExtractor
    from extraction.controllers.website import WebSiteExtractor
    
    # Caminho para o arquivo que será lido
    from utils.config import SITES_FILE_PATH, CHROME_PROFILE_USER


    # Cria uma instancia da classe de gerenciamento do navegador
    webdriver = ChromeDriver()

    # Adiciona perfil de usuário do chrome para instagram
    webdriver.insert_options(user_data_dir=CHROME_PROFILE_USER)

    # Instância de referencia do chromedriver
    browser = webdriver.browser

    # Variavel para controle de sucesso da execução
    execution_successful: bool = False
    
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
                                        
                    ColorManager.info('Iniciando extração de dados do Instagram...')
                    
                    # Cria uma instancia do extrator de instagram
                    instagram_extractor: InstagramExtractor = InstagramExtractor(browser, site)
                    html_text: dict = instagram_extractor.extract_html() # Metodo para extrair os dados do perfil em formato de texto

                    # # Executa a extração de contatos
                    response_ia_instagram: dict = instagram_extractor.extract_contacts(html_text) # Metodo para extrair os contatos do html usando IA
                    
                    # Chamada de metodo para salvar os dados extraidos em planilha excell
                    
                # Se for a landing page da empresa
                else:
                    
                    ColorManager.info('Iniciando extração de dados da landing page...')
                    
                    # Cria uma instancia do extrator de website genérico
                    website_extractor: WebSiteExtractor = WebSiteExtractor(browser, site)
                    data_returned: dict = website_extractor.extract_html() # Metodo para extrair os dados do site
                    response_ia_site: dict = website_extractor.extract_contacts(data_returned) # Metodo para extrair os contatos do html usando IA
                    
                    # Chamada de metodo para salvar os dados extraidos em planilha excell

                    
                    
        # Marca a execução como bem sucedida
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
