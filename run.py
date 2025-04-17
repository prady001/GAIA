# run.py

from agents.dialogo import AgenteDialogo

def main():
    dialogo = AgenteDialogo()

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            print("Sessão encerrada.")
            break

        resposta = dialogo.processar_mensagem(pergunta)
        print(f"Agente: {resposta}")

if __name__ == "__main__":
    main()
