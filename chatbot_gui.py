import streamlit as st
from llama_cpp import Llama

# --------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Assistente de Impressão 3D",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------------------------------
# 1. CARREGAMENTO DO MODELO (COM CACHE)
# --------------------------------------------------------------------------
# O decorador @st.cache_resource garante que o modelo seja carregado apenas
# uma vez, otimizando o desempenho da aplicação.
@st.cache_resource
def load_model():
    """Carrega o modelo LLM e o retorna."""
    try:
        llm = Llama(
            model_path="./Phi-3-mini-4k-instruct-q4.gguf", # <-- Verifique o nome do arquivo
            n_ctx=4096,
            n_gpu_layers=0,
            verbose=False
        )
        return llm
    except Exception as e:
        # Mostra uma mensagem de erro no Streamlit se o modelo não for encontrado
        st.error(f"Erro ao carregar o modelo: {e}", icon="🚨")
        st.stop() # Interrompe a execução do app se não puder carregar o modelo

# Exibe uma mensagem enquanto o modelo está sendo carregado
with st.spinner("Carregando o especialista em Impressão 3D... Por favor, aguarde."):
    llm = load_model()

# --------------------------------------------------------------------------
# 2. DEFINIÇÃO DO CONTEXTO E INICIALIZAÇÃO DO CHAT
# --------------------------------------------------------------------------
# Define a persona do chatbot
system_message = (
    "Você é um assistente especialista em impressão 3D. "
    "Sua missão é ajudar usuários, desde iniciantes até avançados, com suas dúvidas. "
    "Responda de forma clara, didática e objetiva. Forneça dicas práticas sobre filamentos, "
    "configurações de fatiadores (slicers), solução de problemas comuns (como stringing, warping) e manutenção de impressoras."
)

# Título da aplicação que aparece na página
st.title("🤖 Assistente de Impressão 3D")
st.caption("Pergunte-me qualquer coisa sobre o universo da impressão 3D!")

# Inicializa o histórico da conversa no estado da sessão, se ainda não existir.
# Isso garante que o histórico persista entre as interações do usuário.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe todas as mensagens do histórico na interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------------------------------
# 3. LÓGICA DE INTERAÇÃO DO CHAT
# --------------------------------------------------------------------------
# Cria um campo de entrada de texto no rodapé da página.
# O que o usuário digitar aqui será armazenado na variável 'prompt'.
if prompt := st.chat_input("Qual é a sua dúvida sobre impressão 3D?"):
    # Adiciona a mensagem do usuário ao histórico e exibe na tela
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara para gerar a resposta do assistente
    with st.chat_message("assistant"):
        # Mostra um ícone de "pensando" enquanto a resposta é gerada
        with st.spinner("Pensando..."):
            # Prepara a conversa para o modelo, incluindo a instrução do sistema
            conversation_for_model = [
                {"role": "system", "content": system_message}
            ] + st.session_state.messages

            # Chama o modelo para obter a resposta
            response = llm.create_chat_completion(
                messages=conversation_for_model,
                max_tokens=500,
                stop=["<|end|>", "<|user|>"],
                temperature=0.7,
                stream=False # Desativar stream para respostas completas
            )

            # Extrai e exibe a resposta
            assistant_message = response['choices'][0]['message']['content'].strip()
            st.markdown(assistant_message)

    # Adiciona a resposta do assistente ao histórico da conversa
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})