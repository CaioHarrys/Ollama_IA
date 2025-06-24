# Ollama_IA 🚀🧠

Repositório para integração e uso local de modelos de linguagem (LLMs) através do **[Ollama](https://ollama.com/)**, uma plataforma que permite rodar modelos de IA diretamente no seu computador, sem depender da nuvem.

---

## 📜 Descrição

Este projeto demonstra como utilizar a API do Ollama para interagir com modelos de linguagem de forma local via Python.

Com este script, você pode enviar perguntas ou comandos para um modelo AI rodando na sua máquina, obtendo respostas rapidamente, com total controle dos dados e sem necessidade de conexão externa.

---

## 🛠️ Tecnologias e Ferramentas

- 🐍 **Python 3.10+**
- 🔗 **API REST do Ollama**
- 📦 **Bibliotecas Python:**
  - `requests`

---

## 🚀 Instalação e Execução

### 🔧 Pré-requisitos
- Ter o **[Ollama](https://ollama.com/) instalado** na sua máquina (Windows, macOS ou Linux).
- Ter um modelo baixado (ex.: `llama3`, `mistral`, `phi`, `llama2`, etc.).

### 📥 Clone o repositório:

git clone https://github.com/CaioHarrys/Ollama_IA.git
cd Ollama_IA

## 📦 Instale as dependências:
- `pip install -r requirements.txt`

## ▶️ Execute o script:
- `python main.py`
## ⚙️ Como usar
- No arquivo main.py, você pode definir:

🔸 O modelo que deseja utilizar (ex.: "llama3", "mistral", "llama2").

🔸 A mensagem ou comando que será enviado ao modelo.
## 🎯 Exemplo:
`model = "llama3"`
`prompt = "Explique o que é aprendizado de máquina de forma simples."`
`response = chat_with_ollama(model, prompt)`
`print(response)`
## 💡 Funcionalidades
- ✅ Envio de prompts para modelos locais.

- ✅ Recebimento de respostas diretamente da API do Ollama.

- ✅ Código simples e direto, fácil de expandir para outros projetos.
## 🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se livre para abrir uma issue ou enviar um pull request.
## 🧑‍💻 Autor
Feito com 💙 por Caio Harrys