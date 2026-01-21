# Módulo de funções mais frequentes e úteis
from utils.config import *

# from models import directories, xpaths, messages
# from utils import browser
from utils.imports import *
from utils.utils_functions.color_manager import ColorManager # Importa classe responsavel pelas saídas personalizadas no console]
from utils.abstract_class import Shape

# inicia uma instância do chrome driver
# webdriver = ChromeDriver().browser
# browser = webdriver.browser

class BrowserUtils(Shape):
    """Classe para interações genéricas com o navegador.
    
    Methods:
        click_element()
        input_text()
        find_element()
        is_page_ready()
    """
    def __init__(self, browser):
        """
        Inicializa o navegador.

        Args:
            browser: Instância do WebDriver.
        """
        self.browser = browser


    def click_element(self, xpath: str, use_js: bool = False) -> None:
        """
        Clica em um elemento usando Selenium ou JavaScript.

        Args:
            xpath (str): XPath do elemento.
            browser (webdriver): Instancia do webdriver do navegador, vem direto do self.
            use_js (bool): Se `True`, utiliza JavaScript para clicar no elemento.
        """ 
        try:

            # Informa qual metodo está sendo executado nesse momento
            self.info_method()
            
            element = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )

            if use_js:
                self.browser.execute_script('arguments[0].click();', element)

            else:
                element.click()

        except Exception as E:
            # Exiba uma mensagem de erro ao executar o metodo
            ColorManager.error(f'Não foi possível clicar no elemento \n ERRO: {E}')
        
    
    def input_text(self, element, text: str, clear_first: bool = False) -> None:
            """
            Insere texto em um campo de entrada.

            Args:
                element (WebElement): Elemento do campo de entrada.
                text (str): Texto a ser inserido.
                clear_first (bool): Se `True`, limpa o campo antes de inserir o texto.
            """

            try:

                # Informa qual metodo está sendo executado nesse momento
                self.info_method()
                
                # Verifica se é para limpar o campo antes de inserir
                if clear_first:
                    element.clear() # Limpa o campo
                
                # Envia o texto para o campo
                element.send_keys(text)
            
            except Exception as E:
                ColorManager.error(f'Erro ao inserir o texto no elemento \nERRO:{E}')


    def find_element(self, xpath: str) -> WebElement:
        """
        Encontra algum elemento pelo xpath dele.

        Args:
            xpath (string): Contem o xpath direto para o elemento no DOM.
            browser (webdriver): Recebe uma instancia do webdriver do navegador.

        Return:
            element: Objeto webdriver que representa o elemento no DOM html

        Example:
            >>> object.find_element('id=[...]')
            <webdriver.element....>
        """
        try:
            
            # Informa qual metodo está sendo executado nesse momento
            self.info_method()

            # Encontra e armazena o elemento
            element = WebDriverWait(self.browser, 60).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )

            ColorManager.success('Encontrou o elemento com sucesso!')

            return element
        
        except Exception as E:
            ColorManager.error(f'Não foi possível encontrar o elemento \n ERROR: {E}')


    def execute_key(self, value: int, key: str) -> None:
        """
        Executa as teclas recebidas como parametro, dinamicamente durante a chamada da função.

        Args:
            value (int): Valor dinamico, é a quantidade de vezes que a tecla devera ser executada pelo loop abaixo.
            key (string): Uma string representando a tecla que deve ser teclada, usada para adicionar dinamicamente a tecla abaixo.
            browser (webdriver): Recebe uma instancia do webdriver do navegador.

        Example:
            >>> execute_key(4, 'TAB')
            Clica no tab x4
        """
        # Informa qual é o metodo a ser executado
        self.info_method()

        try:
            action = ActionChains(self.browser) # Instancia o actionChains
            
            # Dicionario para armazenar o que cada parametro representa
            key_map = {"TAB": keys.TAB, "ENTER": keys.ENTER}

            # Caso o parametro recebido não seja valido
            if key not in key_map:
                raise ValueError(f'Tecla {key} não suportada.')

            ColorManager.info(f'Executando {key} por {value} vezes...')

            # Executa a tecla determinada quantidade de vezes
            for _ in range(value):
                action.send_keys(key_map[key])               

            action.perform() # Finaliza a instancia do action chains
        
        except Exception as E:
            ColorManager.error(f'Não foi possível executar as teclas\n ERRO: {E}')


class BrowserActions(Shape):
    """
    Classe para ações específicas no navegador
    
    Methods:
        is_page_ready(self)
        open_new_window(self)
    """
    
    def __init__(self, browser):
        """
        Inicializa o navegador.

        Args:
            browser: Instância do WebDriver.
        """
        self.browser = browser


    def is_page_ready(self) -> bool:
        """Verifica se a pagina web aberta na instância do navegador já foi carregada completamente pelo status do DOM."""
        try:
            
            # Informa qual metodo está sendo executado nesse momento
            self.info_method()

            return self.browser.execute_script('return document.readyState') == 'complete'

        except Exception as E:
            ColorManager.error(f'Não foi possível verificar o estado de carregamento da pagina atual\n ERRO: {E}')


    def open_new_window(self, site: str) -> None:
        """
        Abre uma nova aba no navegador utilizando java script.

        Args:
            site (string): Recebe o URL para o site que devera ser aberto na nova aba que foi aberta.
            browser (webdriver): Recebe uma instancia do webdriver do navegador.

        Example:
            >>> open_new_window('https://google.com.br')
            Abre uma nova janela e entra no google.
        """
        # Informa qual metodo está sendo executado no momento
        self.info_method()

        try:
            
            time.sleep(2)

            # Abre uma nova janela no navegador
            self.browser.execute_script("window.open('');")

            time.sleep(3)

            # Alterna o olhar para essa nova janela que foi aberta
            self.browser.switch_to.window(self.browser.window_handles[1])

            # Abre o site na nova janela aberta
            self.browser.get(site)

            # Volta para a janela inicial
            self.browser.switch_to.window(self.browser.window_handles[0])

            # Fecha a janela inicial
            self.browser.close()

            # Agora que a aba original foi fechada, alternar para a aba restante
            self.browser.switch_to.window(self.browser.window_handles[0])

            time.sleep(5)
            
        except Exception as E:
            ColorManager.error(f'Não foi possível abrir uma nova janela no navegador\n ERROR: {E}')


        
            


    
