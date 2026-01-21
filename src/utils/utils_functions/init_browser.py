from utils.config import *
from utils.imports import *

# ------------------------------------------------------------------------
# CONFIGURAÇÃO DE WEBDRIVER
# ------------------------------------------------------------------------

# # Configure o chrome options abaixo...

# # Inicializando o WebDriver usando o webdriver-manager
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class ChromeDriver:
    """
    Classe que gerencia a instância do WebDriver Chrome, configurando e controlando o navegador para automação de tarefas.

    Imports:
        from utils.config import *: Importa configurações de ambiente (não especificadas no trecho de código).
        from utils.imports import *: Importa bibliotecas necessárias, como o Selenium e outros utilitários.

    Parameters:
        Nenhum

    Functions:
        __init__(self, options=None):
            - Inicializa uma instância do WebDriver do Chrome com as opções fornecidas ou padrões.

        launch_browser(self, link):
            - Abre uma página no navegador com o URL especificado.

        kill_browser(self):
            - Finaliza a instância atual do WebDriver, fechando o navegador.

        insert_options(self, download_directory=None, headless=False, disable_gpu=False, user_agent=None):
            - Configura opções personalizadas para o WebDriver, como:
                - Modo headless (sem interface gráfica)
                - Desativação de GPU
                - Alteração do User-Agent
                - Configuração do diretório de downloads
            - Recria a instância do WebDriver com as novas opções.

    Exceptions:
        Não há exceções explícitas definidas, mas pode lançar erros relacionados à configuração do WebDriver ou falhas de comunicação com o Chrome.

    Example:
        >>> driver = ChromeDriver()
        >>> driver.launch_browser("https://www.example.com")
        >>> driver.insert_options(headless=True)
        >>> driver.kill_browser()
    """
    # Metodo para retornar a instancia do webdriver assim que instanciar um objeto da classe
    def __init__(self, options=None):

        # Inicializa o Chrome com opções personalizadas, se forem fornecidas
        chrome_options = options or Options()

        # Inicializando o WebDriver usando o webdriver-manager
        self.browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        print(f'{Fore.GREEN}Iniciando instancia do webdriver...{Fore.RESET}')

    # Metodo utilizado para abrir alguma pagina
    def launch_browser(self, link):

        # Inicializa o navegador
        self.browser.get(link)

        # Exibe uma mensagem alertando sobre ter aberto o site com sucesso
        print(
            f'{Fore.GREEN}Instância do webdriver iniciada com sucesso no site passado!{Fore.RESET}'
        )

    # Metodo que fecha a instancia do navegador
    def kill_browser(self):

        # Finaliza o navegador
        self.browser.quit()

        # Exibe uma mensagem alertando sobre o navegador ter sido finalizado
        print(
            f'{Fore.GREEN}Instância do webdriver foi finalizada com sucesso!{Fore.RESET}'
        )

    # Método para configurar opções no WebDriver
    def insert_options(
        self,
        download_directory=None,
        headless=False,
        disable_gpu=False,
        user_agent=None
    ):
        # Esse metodo sempre que chamado, fecha a instancia atual do navegador e cria uma nova instância com as opções configuradas

        # Inicia uma instância do chrome options
        chrome_options = Options()

        # Configura o modo headless
        if headless:
            chrome_options.add_argument('--headless')
            print(f'{Fore.YELLOW}Modo headless ativado{Fore.RESET}')

        # Desabilitar a GPU
        if disable_gpu:
            chrome_options.add_argument('--disable-gpu')
            print(f'{Fore.YELLOW}Modo GPU desativado{Fore.RESET}')

        # Adicionar um User-Agent personalizado
        if user_agent:
            chrome_options.add_argument(f'user-agent={user_agent}')
            print(
                f'{Fore.YELLOW}User-Agent personalizado adicionado: {user_agent}{Fore.RESET}'
            )

        # Adicionar o diretorio para download padrão
        if download_directory:
            chrome_options.add_experimental_option(
                'prefs', {'download.default_directory': download_directory}
            )
            print(
                f'{Fore.YELLOW}Configurada pasta de download padrão.{Fore.RESET}'
            )

        # Atribuir as opções configuradas ao navegador
        self.browser.quit()  # Finaliza o navegador atual

        self.browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        print(
            f'{Fore.GREEN}Opções configuradas e nova instância do WebDriver iniciada.{Fore.RESET}'
        )