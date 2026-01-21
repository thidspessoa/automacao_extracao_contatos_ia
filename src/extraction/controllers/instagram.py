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

    def extract_profile_data(self) -> dict:
        """Extrai dados do perfil do Instagram dado a URL do perfil"""
        try:

            super().info_method('extract_profile_data')

            profile_data: dict = {}  # Dicionario para armazenar os dados do perfil

            self.browser.get(self.site_url)
            time.sleep(5)  # Aguarda o carregamento da página

            # Clica em fechar o pop-up de registro de conta, se aparecer, usando actions chains, clicando na tecla enter
            actions = ActionChains(self.browser)
            actions.send_keys(Keys.ENTER).perform()

            # Aguarda alguns segundos para garantir o carregamento completo
            time.sleep(3)

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

            # Exibe o html do heaader para debug
            ColorManager.info(
                f"Header HTML: {header_html.prettify() if header_html else 'N/A'}")
            time.sleep(1000)  # Pausa para debug

            if header_html:

                # Obtem o texto separado por espaços
                header_text = header_html.get_text(
                    separator=' ', strip=True) if header_html else 'N/A'

                # Armazena o texto dentro do dicionario
                profile_data['header_text'] = header_text

                # Encontra todas as tags de link dentro do header
                links = header_html.find_all('a', href=True)

                # Itera sobre cada link encontrado
                for a in links:
                    ColorManager.info(f"Analisando link: {a}")
                    href = a['href']

                    # Verifica se o link começa com o redirect padrão do instagram
                    if href.startswith('https://l.instagram.com/'):

                        # Quebra a URL em partes
                        parsed_url = urllib.parse.urlparse(href)

                        # Extrai os parâmetros da query
                        query_params = urllib.parse.parse_qs(parsed_url.query)

                        # Obtém o link real do parâmetro 'u'
                        if 'u' in query_params:

                            # O link real está na primeira posição da lista, decodificamos com unquote
                            real_link_decoded = urllib.parse.unquote(
                                query_params['u'][0])  # LInk real limpo e utilizável

                            # Verifica se de fato o link é para redirecionamento ao whatsapp
                            if 'wa.me' in real_link_decoded or 'whatsapp' in real_link_decoded.lower():
                                profile_data['whatsapp_link'] = real_link_decoded
                                ColorManager.warning(
                                    f"Link do WhatsApp encontrado: {real_link_decoded}")
                                # time.sleep(1000)  # Pausa para debug
                                # break

            else:
                ColorManager.error("Header não encontrado.")

            return profile_data

        except Exception as e:
            raise Exception(f"Erro ao extrair dados do perfil: {e}")
