import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

# Inicializa os módulos
ouvido = sr.Recognizer()
yoda = pyttsx3.init()


def falar(frase):
    print(f"{frase}")
    yoda.say(frase)
    yoda.runAndWait()


def executar_comando(comando):
    comando = comando.lower().replace("lula", "").strip()

    if "encerrar" in comando:
        falar("Encerrando por agora. Que a Força esteja com você.")
        exit()

    elif "horas" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        falar(f"A hora atual é {hora}")

    elif "data" in comando:
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
        falar(f"A data de hoje é {data_atual}")

    elif "pesquise" in comando:
        pesquisa = comando.replace("pesquise", "")
        wikipedia.set_lang("pt")
        try:
            resposta = wikipedia.summary(pesquisa, 2)
            print(resposta)
            falar(resposta)
        except:
            falar("Não consegui encontrar nada sobre isso.")
    elif comando:
        falar("Desculpe, não entendi o comando.")
    elif "tocar" in comando:
        conteudo = comando.replace("tocar", "").strip()
        resposta = pywhatkit.playonyt(conteudo)
        yoda.say(resposta)
        yoda.runAndWait()


def ouvir():
    with sr.Microphone() as mic:
        ouvido.adjust_for_ambient_noise(mic)  # Ajusta para o ruído do ambiente
        print("🎙️ Aguardando comando com 'lula'...")

        try:
            audio = ouvido.listen(mic, timeout=None, phrase_time_limit=5)
            comando = ouvido.recognize_google(audio, language="pt-BR").lower()
            print(f"{comando}")

            if "lula" in comando:
                executar_comando(comando)
            else:
                print("🔇 Palavra-chave não detectada. Ignorando...")

        except sr.UnknownValueError:
            print("🤷‍♂️ Não entendi o que você disse.")
        except sr.RequestError:
            print("❌ Erro ao acessar o serviço de voz.")
        except Exception as e:
            print(f"⚠️ Erro inesperado: {e}")


# LOOP INFINITO
if __name__ == "__main__":
    while True:
        ouvir()
