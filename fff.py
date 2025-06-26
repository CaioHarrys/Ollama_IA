import pyttsx3
import speech_recognition as sr

ouvido = sr.Recognizer()  # Inicializa o reconhecedor de voz
voz = pyttsx3.init()  # Inicializa o sintetizador de voz


def falar(texto):
    print(f"Falando: {texto}")  # Exibir o texto que será falado
    voz.say(texto)  # Dizer o texto
    voz.runAndWait()  # Rodar a fala e esperar até que termine


def ouvir():  # Função para ouvir o comando de voz
    with sr.Microphone() as mic:
        print("Estou ouvindo...")
        ouvido.listen(mic)
        audio = ouvido.listen(mic)
        try:
            comando = ouvido.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            falar("Desculpe, não consegui entender o que você disse.")
            return ""
        except sr.RequestError:
            print("Erro ao se conectar ao serviço de reconhecimento de voz.")
            falar("Desculpe, houve um erro ao tentar reconhecer sua fala.")
            return ""


# falar("Olá, eu sou o Yoda, seu assistente virtual. Como posso ajudar?") # Fala inicial

# ouvir() # Chama a função para ouvir o comando de voz

# Aqui você pode adicionar lógica para processar o comando recebido
# Por exemplo, se o comando for "olá", você pode responder com uma saudação
# if "olá" in comando:
#     falar("Olá! Como posso ajudar você hoje?")
