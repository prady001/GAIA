class AgenteAnalise:
    def __init__(self):
        pass

    def obter_dados(self, tipo):
        if tipo == "clima":
            return {"temperatura": 22, "umidade": 75}
        elif tipo == "poluição":
            return {"co2": 400, "particulas": 35}
        else:
            return {"erro": "Tipo de dado desconhecido"}