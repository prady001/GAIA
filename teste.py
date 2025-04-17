from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")
resposta = llm.invoke("Qual o maior desafio ambiental do Brasil hoje?")
print(resposta)
