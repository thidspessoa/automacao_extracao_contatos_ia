
# Módulo de funções mais frequentes e úteis
from utils.config import *

# from models import directories, xpaths, messages
# from utils import browser
from utils.imports import *
from utils.utils_functions.color_manager import ColorManager # Importa classe responsavel pelas saídas personalizadas no console]
from utils.abstract_class import Shape


class MoveFiles(Shape):
    """
    Classe que possui metodos de manipulação de diretorio de arquivos.
    
    Methods:
        cut_files(self)
        move_files(self)
    """
    def __init__(self, source: str, destination: str):
        self.source = source # Caminho atual do arquivo
        self.destination = destination # Caminho de destino do arquivo


    def cut_files(self) -> None:     # Função para recortar todos os arquivos da pasta para o destino
        """
        Recorta arquivos de uma pasta origem para uma pasta de destinio.

        Args:
            source (string): Contem o caminho de origem do arquivo.
            destination (string): Contem o caminho de destino do arquivo.

        Example:
            >>> cut_files('c:..origem/', 'c:... destino')
            Recorta o arquivo da pasta de origem para a pasta de destino.
        """
        # Informa qual metodo está sendo executado
        self.info_method()
        
        try:
            files = os.listdir(self.source)

            for file in files:
                source_path = os.path.join(self.source, file)
                destination_path = os.path.join(self.destination, file)
                shutil.move(source_path, destination_path)
                ColorManager.success(f'Arquivo {file} movido para {self.destination}')

        except Exception as E:
            ColorManager.error(f'Não foi possível recortar o arquivo para a pasta de destino\n ERRO: {E}')


    def move_files(self) -> None:    # Função para mover arquivos da origem para o destino
        """
        Move o arquivo da pasta de destino para outra pasta de destino (final).

        Args:
            destination (string): Contem o diretorio para a primeira pasta de destino.
            source (string): Contem o diretorio para a segunda pasta de destino (final).

        Example:
            >>> move_files('c:..destino 1/', 'c:... destino 2/')
            Move o arquivo para o destino 1 e por fim para o destino 2.
        """
        # Metodo que exibe informações do metodo que está sendo executado no momento
        self.info_method()

        try:
            # Verifica se o arquivo existe no diretório de origem antes de tentar mover
            for file in os.listdir(self.source):

                source_file = os.path.join(self.source, file)
                destination_file = os.path.join(self.destination, file)

                if os.path.exists(source_file):

                    # Move o arquivo
                    shutil.move(source_file, destination_file)
                    ColorManager.success(f'Arquivo {file} movido para {destination_file}')

                else:

                    ColorManager.info(f'O arquivo {file} não existe no diretorio de origem.')

        except Exception as e:
            # Se houver um erro ao tentar mover arquivos, exibe a mensagem de erro
            ColorManager.error(f'Erro ao tentar mover os arquivos para a pasta de destino\n ERROR: {e}')


# Essa classe não herda a classe abstrata pois ela possui metodos que recebem muitos parametros especificos, não sendo possível instancia-los de forma generalizada
class SaveDeleteFiles:
    """
    Metodos para salvar e deletar arquivos.
    
    Methods:

    """
    def describe(cls) -> str: 
        """Metodo que informa a respeito do metodo que está sendo executado e de qual classe ele faz parte, no console."""
        # Obtém o nome do método que está sendo executado
        actual_method = inspect.currentframe().f_code.co_name
        print(f'*******<<File: {str(os.path.basename(__file__))} | Class:  SaveDeleteFiles | Method: {actual_method}>>*******')

    @classmethod
    def save_unique_file(cls, base_group: list, comercial_path: str, partners_path: str, person_type: str, filtered_df) -> None: # Função para salvar arquivos únicos para cada comercial/parceiro
        """
        Salva um arquivo para cada nome de comercial contido na base passada por parametro.

        Args:
            base_group (Lista): Uma lista que contem o nome de todos os comerciais ou todos os parceiros.
            filtered_df (data frame): Um data frame já limpo e filtrado, é o mesmo arquivo que será enviado aos parceiros e comerciais.
            person_type (String): Um valor que indica qual é o tipo da pessoa (Comercial ou parceiro).
            comercial_path (String): O caminho para o diretorio de arquivos de comerciais.
            partners_path (String): O caminho para o diretorio de arquivos de parceiros.

        Example:
            >>> save_unique_file(comerciais, df_filtrado, 'Comercial')
            ../NOME_COMERCIAL.xlsx
        """
        # Metodo que diz qual o metodo que está executado no momento
        cls.describe()

        try:
            # Salva um arquivo para cada pessoa na planilha
            for person in base_group:
                person_data = filtered_df[filtered_df[person_type] == person]
                person.strip()
                ColorManager.info(person)
                file_name = f'{person}.xlsx'
                file_name = re.sub(r'[<>:"/\\|?*]', '', file_name)

                if person_type == 'Comercial':
                    commercial_file = os.path.join(
                        comercial_path, file_name
                    )
                    person_data.to_excel(commercial_file, index=False)
                    ColorManager.success(f'Arquivo salvo: {commercial_file}')

                elif person_type == 'Parceiros':
                    partner_file = os.path.join(
                        partners_path, file_name
                    )
                    person_data.to_excel(partner_file, index=False)
                    ColorManager.successt(f'Arquivo salvo: {partner_file}')

        except Exception as E:
            ColorManager.error(
                f'Não foi possível salvar um arquivo individual para cada pessoa da planilha\n ERROR: {E}'
            )

    
    @classmethod
    def capture_path_base(cls, directory: str) -> str: # Função para retornar o caminho do arquivo base 
        """
        Função para retornar o caminho do arquivo base no formato `.xlsx` em um diretório especificado.

        Imports:
            from utils import error: Função personalizada para exibir mensagens de erro.
            os: Módulo para interação com o sistema de arquivos.

        Parameters:
            directory (str): O diretório onde procurar pelo arquivo base.

        Returns:
            str: O caminho completo do primeiro arquivo `.xlsx` encontrado no diretório.

        Exceptions:
            Se ocorrer algum erro durante a execução, a função exibe uma mensagem de erro detalhada.

        Example:
            >>> capture_path_base('/caminho/para/diretorio')
            '/caminho/para/diretorio/arquivo_base.xlsx'
        """
        # Importação de submodulos e recursos necessários
        from utils import error, click_element, input_text, verify_input_content, info
        # Metodo que diz qual o metodo que está sendo executado no momento
        cls.describe()

        try:
            
            # lista todos os arquivos no diretorio base
            list_name_files_directory = os.listdir(directory)

            if len(list_name_files_directory) > 0:

                info(list_name_files_directory)

                # Obtem o caminho do arquivo base principal no diretorio base
                for file in list_name_files_directory:

                    # Verifica se a extensão do arquivo listado no diretorio é xlsx
                    if file.endswith('.xlsx'):

                        # Salva o caminho do arquivo
                        file_base = os.path.join(directory, file)

                # Retorna o caminho para o relatorio do excel
                return file_base    

            else: 
                raise FileNotFoundError(f'Não existe nenhum arquivo na pasta de arquivos base!')    
            
        except Exception as E:
            # Exibe uma mensagem de falha padronizada
            ColorManager.error(f"Não foi possível obter o caminho para o arquivo base\nERRO: {E}")