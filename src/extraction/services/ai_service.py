from utils.utils_functions.color_manager import ColorManager
from utils.imports import *
from utils.config import GEMINI_API_KEY
from utils.abstract_class import Shape

class AIService(Shape): 
    
    def __init__(self):
        """
        Docstring para __init__

        """
        super().__init__()  # Chama o construtor da classe abstrata que já obtem o nome do arquivo
        self.client = genai.Client(api_key=GEMINI_API_KEY)


    def call_ia (self, prompt: str) -> str:
        """
        Chama o serviço de IA para processar o prompt dado
        
        - Nunca retorna string
        - Nunca retorna objeto bruto da SDK
        - Nunca propaga erro para camadas superiores

        :param prompt: Prompt a ser enviado para a IA
        :type prompt: str
        :return: Resposta da IA
        :rtype: str
        """
        try:
            
            # Log padronizado informando qual método está sendo executado
            super().info_method('call_ia')

            # Chamada à API do Gemini para geração de conteúdo
            response = self.client.models.generate_content(
                model="models/gemini-flash-latest",  # Modelo rápido e barato
                contents=prompt,                     # Prompt enviado pelo extractor
                config=genai.types.GenerateContentConfig(
                    temperature=0.1,                 # Baixa aleatoriedade (resposta mais estável)
                    max_output_tokens=2048            # Limite de tokens de saída
                )
            )

            # Extrai o texto puro retornado pela IA
            raw_text: str = response.text.strip()

            ColorManager.warning(f"Resposta bruta da IA: {raw_text}")

            # Usa regex para localizar um bloco JSON válido dentro do texto
            # Isso protege contra respostas com texto extra antes/depois do JSON
            match: re.Match = re.search(r"\{.*\}", raw_text, re.DOTALL)

            # Se não encontrar um JSON válido, retorna estrutura vazia segura
            if not match:
                return self._empty_response()

            # Converte o JSON (string) em dicionário Python
            return json.loads(match.group())
        
        except Exception as e:
            # Qualquer erro (API, JSON inválido, timeout, etc.)
            # retorna um dicionário vazio padronizado
            return self._empty_response()
            


    @staticmethod
    def _empty_response() -> dict:
        """
        Retorna um dicionário vazio padronizado.
        Garante que o contrato com o restante do sistema seja mantido.
        """
        return {
            "emails": [],
            "telefones": [],
            "whatsapp": [],
            "nome_empresa": ""
        }
