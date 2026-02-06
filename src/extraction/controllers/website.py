"""
Esse arquivo contem o controller para extração de dados do Instagram
"""

from utils.utils_functions.color_manager import ColorManager
from utils.imports import *
from utils.abstract_class import Shape
from selenium.webdriver.common.keys import Keys


class WebSiteExtractor(Shape):
    """Classe para extração de dados do site da empresa"""

    def __init__(self, browser: webdriver.Chrome, site_url: str):
        """
        Docstring para __init__

        :param browser: Descrição
        :type browser: webdriver.Chrome
        :param site_url: Link do site da empresa
        :type site_url: str
        """
        self.browser = browser
        self.site_url = site_url
        super().__init__()  # Chama o construtor da classe abstrata que já obtem o nome do arquivo

    def extract_html(self) -> dict:
        """
        Extraí o HTML do site da empresa dado a URL do site

        :param browser: none 
        :type browser: none
        """
        try:

            super().info_method('extract_html')
            data: dict = {}  # Dicionario para armazenar os dados extraídos

            # self.browser.set_page_load_timeout(60)

            try:
                self.browser.get(self.site_url)
            except TimeoutException:
                ColorManager.warning(f'Timeout ao carregar {self.site_url}')
                return {"html_text": ""}

            time.sleep(10)

            # Pega o HTML da pagina comb bs4
            soup: BeautifulSoup = BeautifulSoup(
                self.browser.page_source, 'html.parser')

            # Pega todo o texto do html recuperado pelo bs4
            html_text: str = soup.get_text(separator=' ', strip=True)
            
            
            print('Dados da landing page: ' + html_text)

            # Remove linhas em branco excessivas
            # Separa o texto em linhas
            lines: list = (line.strip() for line in html_text.splitlines())
            chunks: list = (phrase.strip() for line in lines for phrase in line.split(
                "  "))  # Separa o texto em pedaços menores
            # Junta tudo de volta, removendo linhas vazias
            text: str = '\n'.join(chunk for chunk in chunks if chunk)

            # Truncar o texto se for muito grande para evitar estourar o limite de tokens
            # Geralmente contatos estão no rodapé ou no início da página, 15k caracteres costuma ser suficiente
            # Truncar é o processo de cortar o texto para um tamanho máximo
            text = text[:15000]

            # Salva no dicionario de dados
            data['html_text'] = text

            return data

        except Exception as e:
            raise Exception(f"Erro ao extrair dados do site: {e}")

    def extract_contacts(self, data: dict) -> dict:
        """
        Captura os dados da empresa em meio ao HTML extraído usando IA

        :param data: Dicionario contendo o HTML extraído
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
