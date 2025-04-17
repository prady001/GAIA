# agents/dialogo.py

from agents.consultoria import AgenteConsultoria
from agents.analise_dados import AgenteAnalise

class AgenteDialogo:
    def __init__(self):
        self.consultoria = AgenteConsultoria()
        self.analise = AgenteAnalise()
    
    def processar_mensagem(self, mensagem):
        mensagem = mensagem.lower()  # Tornar tudo minúsculo para simplificar a comparação
        
        # Verificando se a mensagem contém palavras-chave para dados climáticos
        if "clima" in mensagem or "temperatura" in mensagem:
            dados_clima = self.analise.obter_dados("clima")
            return f"Dados climáticos: {dados_clima}"

        # Verificando se a mensagem contém palavras-chave ambientais
        elif "problema ambiental" in mensagem or "maior desafio" in mensagem:
            resposta = self.consultoria.invoke(mensagem)  # Alterado para "invoke"
            return f"Resposta ambiental: {resposta}"

        else:
            return "Desculpe, não entendi sua pergunta. Tente perguntar sobre o clima ou sobre problemas ambientais."
