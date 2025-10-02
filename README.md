# 🤖 Chatbot Especialista Local com IA e Interface Gráfica

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este projeto é um chatbot interativo e personalizável que roda 100% localmente, sem a necessidade de chaves de API ou custos associados. Utilizando um modelo de linguagem de código aberto (LLM) e uma interface gráfica amigável criada com Streamlit, este chatbot pode ser configurado para ser um especialista em qualquer assunto. A versão atual está configurada como um **especialista em Impressão 3D**.

## 📸 Demonstração


![Demo do Chatbot](chatbot.png)


## ✨ Principais Características

-   **Totalmente Local:** Roda em sua própria máquina, garantindo privacidade e zero custos de API.
-   **Interface Intuitiva:** Interface de chat moderna e responsiva construída com Streamlit.
-   **Persona Customizável:** Facilmente adaptável para ser um especialista em qualquer área (História, Culinária, Programação, etc.) com a alteração de uma única variável.
-   **Rápido e Eficiente:** Utiliza `llama-cpp-python` para uma inferência otimizada do modelo, funcionando bem mesmo em CPUs.
-   **Código Aberto:** Construído com ferramentas open-source, desde o modelo de linguagem até as bibliotecas.

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3.9+
-   **Interface Gráfica:** Streamlit
-   **Modelo de Linguagem (LLM):** Microsoft Phi-3-mini (formato GGUF)
-   **Backend do Modelo:** llama-cpp-python

## 🚀 Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

-   Python 3.9 ou superior
-   Git

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/ViniciuscRodrigues/simplechatbot.git](https://github.com/ViniciuscRodrigues/simplechatbot.git)
    cd simplechatbot
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Baixe o Modelo de Linguagem (LLM):**
    Este projeto utiliza o modelo `Phi-3-mini-4k-instruct-q4.gguf`.
    -   Faça o download a partir do [Hugging Face](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf).
    -   **Importante:** Coloque o arquivo `.gguf` baixado na **pasta raiz do projeto**, junto com o arquivo `chatbot_gui.py`.

    *(O arquivo do modelo não é incluído neste repositório por ser muito grande).*

5.  **Execute a aplicação:**
    Após a instalação, inicie a interface do Streamlit com o seguinte comando:
    ```bash
    streamlit run chatbot_gui.py
    ```
    Uma nova aba será aberta automaticamente em seu navegador com o chatbot pronto para uso!

## 🔧 Como Customizar a Persona do Chatbot

A "alma" do chatbot está na variável `system_message` dentro do arquivo `chatbot_gui.py`. Para mudar sua especialidade, basta editar o texto desta variável.

**Exemplo (Especialista em Culinária):**
```python
# Dentro de chatbot_gui.py

system_message = (
    "Você é um chef de cozinha renomado e assistente culinário. "
    "Sua missão é dar dicas de receitas, técnicas de cozinha e substituição de ingredientes. "
    "Responda de forma inspiradora, clara e fácil de seguir."
)
```

## 📂 Estrutura do Projeto

```
.
├── .gitignore
├── chatbot_gui.py
├── Phi-3-mini-4k-instruct-q4.gguf  <-- (Baixado manualmente, não no Git)
├── README.md
└── requirements.txt
```

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---
Feito por [Vinicius Caio Rodrigues](https://github.com/ViniciuscRodrigues).