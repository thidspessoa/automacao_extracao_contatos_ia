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

        :param prompt: Prompt a ser enviado para a IA
        :type prompt: str
        :return: Resposta da IA
        :rtype: str
        """
        try:
            
            super().info_method('call_ia')

            # for model in self.client.models.list():
            #     print(model.name)

            # time.sleep(1000)

            # Cria a requisição para a IA
            response: genai.types.GenerateContentResponse = self.client.models.generate_content (
                model= "models/gemini-flash-latest",
                contents=prompt,
                config=genai.types.GenerateContentConfig (
                    temperature=0.1,
                    max_output_tokens=2048
                )
            )

            print(type(response)) # Exibe o tipo da resposta para debug
            print(response) # Exibe a resposta completa para debug
            
            return response.text
        
        except Exception as e:
            raise Exception(f"Erro ao requisitar o serviço de IA: {e}")