import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

ouvido = sr.Recognizer()
yoda = pyttsx3.init()

def executar_comando():
    try:
        with sr.Microphone() as mic:
            print("Estou ouvindo...")
            voz = ouvido.listen(mic)
            comando = ouvido.recognize_google(voz, language="pt-BR")
            comando = comando.lower()  # Converte o comando para minúsculas

            if 'Lula' in comando:
                comando = comando.replace('Lula', '')
                yoda.say(comando)
                yoda.runAndWait()
           
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o que você disse.")
    except sr.RequestError:
        print("Erro ao se conectar com o serviço de reconhecimento de voz.")

    return comando

def realizar_acao():
    comando = executar_comando()

    if 'horas' in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        yoda.say(f"A hora atual é {hora} seu pedaço de merda mole")
        yoda.runAndWait()
    elif 'data' in comando:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
        yoda.say(f"A data de hoje é {data_atual}")
        yoda.runAndWait()
    elif 'pesquise' in comando:
        pesquisa = comando.replace('pesquise', '')
        wikipedia.set_lang("pt")
        resposta = wikipedia.summary(pesquisa, 2)
        print(resposta)
        yoda.say(resposta)
        yoda.runAndWait()
    elif comando:
        yoda.say("Desculpe, não entendi o comando.")
    else:
        print("Nenhum comando reconhecido.")

    yoda.runAndWait()

# Exemplo de execução contínua
# while True:
realizar_acao()
