# Módulo de funções mais frequentes e úteis
from utils.config import *

# from models import directories, xpaths, messages
# from utils import browser
from utils.imports import *
from utils.utils_functions.color_manager import ColorManager # Importa classe responsavel pelas saídas personalizadas no console

# inicia uma instância do chrome driver
# webdriver = ChromeDriver().browser
# browser = webdriver.browser

# --------------------------------------------------------------------------

class WhatsappFileUtils:
    """
    Classe responsavel por mainipular arquivos no whatsapp.

    Methods:
        attach_file_whatsapp(browser, file, person_type, wpp_number, file_name)
    """
    def describe(cls) -> str: 
        """Metodo que informa a respeito do metodo que está sendo executado e de qual classe ele faz parte, no console."""
        # Obtém o nome do método que está sendo executado
        actual_method = inspect.currentframe().f_code.co_name
        print(f'*******<<File: {str(os.path.basename(__file__))} | Class:  SaveDeleteFiles | Method: {actual_method}>>*******')


    @classmethod
    def attach_file_whatsapp(cls, browser, file, person_type, wpp_number, file_name):     # Função para anexar documentos no WhatsApp
        """
        Envia o arquivo final ja tratado, para: Comerciais, parceiros e assistentes no Whatsapp.

        Args:
            browser (webdriver): Contem uma instância do objeto da classe de gerenciamento do webdriver chrome.
            file (string): Contem o caminho direto para o arquivo (tipo_pessoa.xlsx).
            person_type (string): Contem o tipo da pessoa (Comercial, assistente, parceiro).
            wpp_number (string): Contem o número do whatssap da pessoa.
            file_name (string): Armazena o nome do arquivo (nome_pessoa.xlsx).

        Example:
            >>> attach_file_whatssap('c://...arquivo.xlsx', 'Comercial', '819931024213', 'SAMARA REGIANA - PE.xlsx')
            Anexa e envia o arquivo via whatssap junto com a mensagem.
        """
        from models import (
            xpath_wpp_attach_file,
            xpath_wpp_main_page,
            xpath_wpp_documents,
            xpath_wpp_message,
            xpath_wpp_send_attachment,
            xpath_wpp_nonexistent_url,
            message_wpp_default,
            message_wpp_default1,
            message_wpp_confirmation
        )
        from utils.utils_functions.browser_utils import click_element, input_text, find_element, execute_key
        
        # Metodo que informa qual o meotodo que está sendo executado no momento
        cls.describe()
        
        try:
            
            # Verificação se a pagina carregou
            for _ in range(1, 60):

                # Encontra o container que armazena as conversas abertas, para conseguir validar que a pagina carregou
                element_side_chats = find_element('//*[@id="side"]', browser)

                # Alerta do tempo que está sendo eseperado para o navegador carregar a pagina
                ColorManager.info(f'Aguardando até 60 segundos para pagina carregar: {_}')

                # Se encontrar o elemento, então a pagina carregou, quebre o loop
                if element_side_chats:
                    ColorManager.info('Encontrou o elemento, whatsapp aberto com sucesso!')
                    break

                # Aguarda um segundo para poder continuar para a proxima iteração
                time.sleep(1)

            # # ----------------------- DEBUG
            # warning(f'Arquivo sendo passado para o input: {file}\n Nome do arquivo: {file_name}')

            time.sleep(3)

            # Clica no elemento anexar
            click_element(xpath_wpp_attach_file, browser, True)

            ColorManager.info('Clicou no botão anexar')

            time.sleep(1)

            click_element(xpath_wpp_documents, browser, True)

            ColorManager.info('Clicou no elemento documents!')

            # Aguarda até que o elemento esteja presente no DOM e visível
            document_element = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
            )

            # Campo de input para inserir o caminho do arquivo
            document_element.send_keys(file)

            ColorManager.info(f'Arquivo anexado!')

            time.sleep(3)
            
            # Procura o campo de envio de mensagem
            message_caption_element = find_element("p.selectable-text.copyable-text", browser, 'css_selector')

            # Digita a mensagem de acordo com o tipo de pessoa (Comercial ou Parceiro)
            if person_type == 'Comercial':
                # Exibe uma saída personalizada no console com a informação passada como parametro
                ColorManager.info('A pessoa é um Comercial')

                # Exibe uma saída de console mostrando a mensagem que será inserida no campo de mensagem
                ColorManager.info(message_wpp_default)

                # Insere a mensagem para enviar junto ao arquivo, no campo de mensagem
                input_text(message_caption_element, message_wpp_default, True)

            elif person_type == 'Parceiro':
                # Exibe uma saída personalizada no console com a informação passada como parametro
                ColorManager.info('A pessoa é um Parceiro')

                # Exibe uma saída personalizada no console com a informação passada como parametro
                ColorManager.info(message_wpp_default1)
                
                # Insere a mensagem para enviar junto ao arquivo, no campo de mensagem
                input_text(message_caption_element, message_wpp_default1, True)

            elif person_type == 'Confirmação':
                # Exibe uma saída personalizada no console com a informação passada como parametro
                ColorManager.info('A pessoa é Assistente')

                # Exibe uma saída personalizada no console com a informação passada como parametro
                ColorManager.info(message_wpp_confirmation)

                # Insere a mensagem para enviar junto ao arquivo, no campo de mensagem
                input_text(message_caption_element, message_wpp_confirmation, True)     

            time.sleep(2)   

            # Clica na tecla enter para enviar a mensagem com o anexo
            execute_key(1, 'ENTER', browser)

            print('Clicou enter')

            time.sleep(5)

        except Exception as E:
            
            # Procura a mensagem de numero  nao existente
            nonexistent_number = find_element(
                xpath_wpp_nonexistent_url, 
                browser
            )

            # Se a mensagem de numero inexistente estiver aparecendo
            if nonexistent_number:
                ColorManager.error(f'Erro ao tentar enviar anexo para o numero: {wpp_number}\nDono(a) do número: {file}')
            
            ColorManager.error(f'Ocorreu um erro ao processar o arquivo: {file_name}\n Erro: {E}')