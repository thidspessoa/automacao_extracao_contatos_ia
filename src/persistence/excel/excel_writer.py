"""
Esse arquivo contem a classe com os metodos para persistência de dados em Excel (.xlsx)
"""

from utils.utils_functions.color_manager import ColorManager
from utils.imports import *
from utils.abstract_class import Shape


class ExcelPersistence(Shape):
    """
    classe para persistência de dados em Excel (.xlsx)
    Methods
    -------
    save_data_to_excel(data: dict, file_name: str) -> None
        Salva os dados fornecidos em um arquivo Excel com o nome especificado.
    """
    
    def __init__(self):
        self.path_file: str = os.getenv("EXCEL_OUTPUT_PATH")  # Variavel para recuperar do arquivo .env o caminho do arquivo excel, que ele será salvo
        super().__init__()  # Chama o construtor da classe abstrata que já obtem o nome do arquivo
    
    def save_data (self, data: list[dict]) -> None:
        """
        Salva os dados fornecidos em um arquivo Excel com o nome especificado.

        :param data: Lista contendo os dicionários com os dados a serem salvos.
        :type data: list[dict]
        :return: None
        """
        try: 
            
            super().info_method('save_data')

            if not data:
                ColorManager.warning('Nenhum dado recebido para persistência.')
                return

            # Garante existência do diretório
            output_dir = os.path.dirname(self.path_file)
            os.makedirs(output_dir, exist_ok=True)
            
            # Normalização: listas -> string
            rows = []
            for item in data:
                rows.append({
                    "Nome da Empresa": item.get("nome_empresa", ""),
                    "Emails": ", ".join(item.get("emails", [])),
                    "Telefones": ", ".join(item.get("telefones", [])),
                    "WhatsApp": ", ".join(item.get("whatsapp", [])),
                })

            df = pd.DataFrame(rows)

            df.to_excel(self.path_file, index=False)

            ColorManager.success(
                f'{len(df)} registros salvos em Excel com sucesso.'
            )

        except Exception as e:
            ColorManager.error(f'Erro ao salvar dados em Excel: {e}')