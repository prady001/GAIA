# Cronograma de Desenvolvimento do Projeto GAIA

## Semana 1

| Dia | Foco                                                                 | Entregas                                                                 |
|-----|----------------------------------------------------------------------|--------------------------------------------------------------------------|
| 1   | Configuração do ambiente e testes com LLM local (Mistral/Yi via Ollama) | `models/model_config.yaml`, setup local funcionando                      |
| 2   | Esboço de arquitetura dos 3 agentes principais                       | Estrutura inicial em `agents/`, diagrama em Miro                         |
| 3   | Criar agente diplomata (busca soluções sociais/políticas em fontes abertas) | `agents/diplomat_agent.py`, RAG básico com ChromaDB                      |
| 4   | Criar agente cientista (analisa dados, estuda impacto ambiental/social) | `agents/scientist_agent.py`, integração com dados reais                  |
| 5   | Criar agente estrategista (propõe plano de ação e impacto)          | `agents/strategist_agent.py`, lógica de orquestração                     |
| 6   | Pipeline de RAG completo (retriever + embedder) usando `rag/`       | `embedder.py`, `retriever.py`, `documents/` com PDFs                     |
| 7   | Integração dos 3 agentes via `run.py` com fluxo simples             | MVP funcional via terminal                                               |

## Semana 2

| Dia | Foco                                                                 | Entregas                                                                 |
|-----|----------------------------------------------------------------------|--------------------------------------------------------------------------|
| 8   | Construir frontend simples com Streamlit ou Gradio                  | `interface/app.py`, chatbot visual                                       |
| 9   | Adicionar entrada por voz com Whisper                               | Reconhecimento de fala no frontend                                       |
|10   | Adicionar saída por voz com Coqui TTS ou Bark                       | GAIA "falando" as soluções geradas                                       |
|11   | Visualizações com mapas, fluxogramas, tabelas                       | Integração de `folium`, `plotly`, `pandas`                               |
|12   | Criar estudo de caso (ex: crise hídrica Yanomami) e rodar pipeline completo | `data/`, screenshots, logs, validação com um mentor                     |
|13   | Finalizar README + documentar o projeto para repositório GitHub    | `README.md` completo, `.md` de cada agente                               |
|14   | Gravar vídeo demo e preparar pitch para apresentação               | Vídeo de 1–2 min, pitch deck opcional em PDF                             |
