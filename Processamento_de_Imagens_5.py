import cv2
import numpy as np

# Insira o diretório onde as imagens estão armazenadas
imagem_em_tons_de_cinza = cv2.imread('C:\\Users\\karat\\Downloads\\A.jpg', cv2.IMREAD_GRAYSCALE) # Deixei as imagens em meu computador, pois dava bug toda vez que eu mudava elas de diretório.

if imagem_em_tons_de_cinza is None:
    print("Não foi possível carregar a imagem em tons de cinza.")
else:
    # Isso encontra os contornos na imagem em tons de cinza
    contornos, _ = cv2.findContours(imagem_em_tons_de_cinza, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Isso cria uma cópia da imagem original para desenhar os contornos
    imagem_com_contornos = cv2.imread('C:\\Users\\karat\\Downloads\\A.jpg') # Insira o diretório onde as imagens estão armazenadas

    # Isso desenha os contornos encontrados na imagem original (usei a cor verde e espessura de linha 2)
    cv2.drawContours(imagem_com_contornos, contornos, -1, (0, 255, 0), 2)

    # Isso exibe a imagem com os contornos desenhados
    cv2.imshow('Imagem com Contornos', imagem_com_contornos)

    cv2.waitKey(0)
    cv2.destroyAllWindows()