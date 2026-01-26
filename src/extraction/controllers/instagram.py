"""
Esse arquivo contem o controller para extração de dados do Instagram
"""

from utils.utils_functions.color_manager import ColorManager
from utils.imports import *
from utils.abstract_class import Shape
from selenium.webdriver.common.keys import Keys


class InstagramExtractor(Shape):
    """Classe para extração de dados do Instagram"""

    def __init__(self, browser: webdriver.Chrome, site_url: str):
        """
        Docstring para __init__

        :param browser: Descrição
        :type browser: webdriver.Chrome
        :param site_url: Link do perfil do instagram
        :type site_url: str
        """
        self.browser = browser
        self.site_url = site_url
        super().__init__()  # Chama o construtor da classe abstrata que já obtem o nome do arquivo

    def extract_html(self) -> dict:
        """Extrai dados do perfil do Instagram dado a URL do perfil"""
        try:

            super().info_method('extract_html')
            profile_data: dict = {}  # Dicionario para armazenar os dados do perfil

            # self.browser.set_page_load_timeout(60)

            try:
                self.browser.get(self.site_url)
            except TimeoutException:
                ColorManager.warning(f'Timeout ao carregar {self.site_url}')
                return {"html_text": ""}

            time.sleep(10)

            # Clica no botão "...mais" na bio, se existr uma tag span com texto 'mais'
            try:
                more_button = self.browser.find_element(
                    By.XPATH, "//span[text()='mais']")
                more_button.click()
                time.sleep(5)  # Aguarda o carregamento do texto completo
            except NoSuchElementException:
                ColorManager.error(
                    'Botão "mais" não encontrado, continuando...')
                pass  # Se o botão não existir, continua normalmente

            soup = BeautifulSoup(self.browser.page_source, 'html.parser')

            # Buscar APENAS a tag header
            header_html = soup.find('header')

            if header_html:

                # Obtem o texto separado por espaços
                header_text = header_html.get_text(
                    separator=' ', strip=True) if header_html else 'N/A'

                # Armazena o texto dentro do dicionario
                profile_data['html_text'] = header_text

                print('Dados do perfil extraídos com sucesso: ' + header_text)

            else:
                ColorManager.error("Header não encontrado.")

            return profile_data

        except Exception as e:
            raise Exception(f"Erro ao extrair dados do perfil: {e}")

    def extract_contacts(self, data: dict) -> dict:
        """
        Captura os dados do perfil em meio ao texto do HTML extraído usando IA

        :param data: Dicionario contendo o texto HTML extraído
        :type data: dict
        """
        # importa a classe de chamadas da API do gemini
        from src.extraction.services.ai_service import AIService

        try:

            super().info_method('extract_contacts')

            prompt: str = f"""
                Extraia informações de contato do texto abaixo.
                
                Responda APENAS com um JSON válido.
                NÃO use markdown.
                NÃO use ```json.
                NÃO adicione explicações.

                Formato exato:
                {{
                    "emails": [],
                    "telefones": [],
                    "whatsapp": [],
                    "nome_empresa": ""
                }}
                
                Texto:
                {data.get('html_text', '')}
            """

            # Chama o metodo da classe responsavel por requisições a IA, que chamara a API do gemini
            ai_service: AIService = AIService()
            ia_response: dict = ai_service.call_ia(prompt) # Resposta da IA em formato de dicionario

            if not isinstance(ia_response, dict):
                raise Exception("Resposta da IA não está no formato esperado de dicionário.")

            ColorManager.info(f"Resposta da IA: {ia_response}")

            
            return ia_response

        except Exception as e:
            raise Exception(f"Erro ao extrair contatos do html usando IA: {e}")