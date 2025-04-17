# agents/consultoria.py

from langchain_ollama import OllamaLLM

class AgenteConsultoria:
    def __init__(self, modelo="mistral"):
        self.llm = OllamaLLM(model=modelo)
    
    def invoke(self, pergunta):  # Alterado de "responder" para "invoke"
        resposta = self.llm.invoke(pergunta)  # Chama o método correto de invocação
        return resposta
