import speech_recognition as sr
from langdetect import detect
from gtts import gTTS
import pygame
import os


class ReconhecerVoz:
    def __init__(self):
        print("Preparando Reconhecimento de voz")
        self.nome_audio = os.path.join(
            os.getcwd(), "audios", "audio.mp3"
        )

    def ouvir_microfone(self):
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            print("Diga alguma coisa em voz alta e bom som...")
            audio = microfone.listen(source)

        try:
            frase = microfone.recognize_google(
                audio, language="pt-BR"
            )
            print(f"Você disse: {frase}")
            return frase
        except sr.UnknownValueError:
            print("Não entendi")
            return 0
        
    def obter_linguagem(self, frase):
        linguagem = detect(frase)
        return linguagem
    
    def criar_audio(self, audio, linguagem):
        try:
            tts = gTTS(audio, lang=linguagem)
        except:
            tts = gTTS(audio)
        tts.save(self.nome_audio)
        print("Reproduzindo o que você disse...")
        pygame.mixer.init()
        pygame.mixer.music.load(self.nome_audio)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock()

        pygame.mixer.quit()
        os.remove(self.nome_audio)


if __name__ == "__main__":
    try:
        r = ReconhecerVoz()
        while True:
            resposta = str(input("\nGostaria de testar? [S/N] "))
            if resposta.upper().strip() == "N":
                break
            elif resposta.upper().strip() == "S":
                frase = r.ouvir_microfone()
                if frase != 0:
                    linguagem = r.obter_linguagem(frase)
                    r.criar_audio(frase, linguagem)
            else: 
                print("Opção inválida")
    except KeyboardInterrupt:
        print("\nPrograma interrompido")
    finally:
       print("\nProcesso finalizado") 
