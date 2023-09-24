import face_recognition
from time import sleep
import mediapipe as mp
import numpy as np
import cv2
import os


class ReconhecerFace:
    def __init__(self):
        print("Preparando Reconhecimento facial")
        self.imagem1 = os.path.join(
            os.getcwd(), "imagens", "imagem1.jpg"
        )
        self.imagem2 = os.path.join(
            os.getcwd(), "imagens", "imagem2.jpg"
        )

    def detectar_rostos(self):
        # Se conectar com a câmera
        webcam = cv2.VideoCapture(0)
        # Ativando reconhecimento
        reconhecimento_rosto = mp.solutions.face_detection
        # Ativando desenho
        desenho = mp.solutions.drawing_utils
        # Detectar rostos na imagem
        reconhecedor_rosto = reconhecimento_rosto.FaceDetection()
        print("\nPressione a tecla ESC para sair")
        sleep(5)
        while webcam.isOpened():
            # Leitura da imagem
            validacao, frame = webcam.read()
            if not validacao:
                break
            imagem = frame
            lista_rostos = reconhecedor_rosto.process(imagem)
            
            if lista_rostos.detections:
                for rosto in lista_rostos.detections:
                    # Cria o desenho na imagem
                    desenho.draw_detection(imagem, rosto)
            
            cv2.imshow("Detecção de rostos", imagem)
            # Clicar na tecla ESC para sair da câmera
            if cv2.waitKey(5) == 27:
                break
        # Encerra a conexão
        webcam.release()
        cv2.destroyAllWindows()
    
    def comparar_rostos(self):
        imagem_referencia = face_recognition.load_image_file(
            self.imagem1
        )
        pontos_referencia = face_recognition.face_landmarks(imagem_referencia)[0]
        imagem_comparacao = face_recognition.load_image_file(
            self.imagem2
        )
        pontos_comparacao = face_recognition.face_landmarks(imagem_comparacao)[0]
        referencia_np = np.array(pontos_referencia["chin"])
        comparacao_np = np.array(pontos_comparacao["chin"])
        distancia = np.linalg.norm(referencia_np - comparacao_np)
        similaridade = 1 - distancia
        print(f"Similaridade: {similaridade}")

if __name__ == "__main__":
    r = ReconhecerFace()
    # r.detectar_rostos()
    r.comparar_rostos()
