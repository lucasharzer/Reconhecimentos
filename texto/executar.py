from dotenv import load_dotenv, find_dotenv
import pytesseract
import cv2
import os


class ReconhecerTexto:
    def __init__(self):
        load_dotenv(find_dotenv())
        print("Preparando Reconhecimento de texto...")
        self.imagem = os.path.join(
            os.getcwd(), "imagens", "imagem.jpg"
        )
        self.caminho_tesseract = os.getenv("TESSERACT_PATH")

    def carregar_imagem(self):
        # Carregar imagem
        imagem = cv2.imread(self.imagem)
        # Melhorar contraste da imagem
        imagem_contraste = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        return imagem_contraste

    def reconhecer_texto(self):
        pytesseract.pytesseract.tesseract_cmd = self.caminho_tesseract
        imagem = self.carregar_imagem()
        texto = pytesseract.image_to_string(imagem)
        return texto


if __name__ == "__main__":
    r = ReconhecerTexto()
    txt = r.reconhecer_texto()
    print("Texto reconhecido na imagem:\n")
    print(txt)
