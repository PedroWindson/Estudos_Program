import cv2
import numpy as np

# Insira o diretório onde as imagens estão armazenadas
imagem_colorida = cv2.imread('C:\\Users\\karat\\Downloads\\A.jpg') # # Deixei as imagens em meu computador, pois dava bug toda vez que eu mudava elas de diretório.

# Verifique se a imagem foi carregada com sucesso
if imagem_colorida is None:
    print("Não foi possível carregar a imagem.")
else:
    imagem_em_tons_de_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

    # Isso cria uma imagem vazia para exibir lado a lado com a outra
    altura, largura = imagem_colorida.shape[:2]
    resultado = np.zeros((altura, largura * 2, 3), dtype=np.uint8)

    # Colocando a imagem colorida e a imagem em tons de cinza no resultado
    resultado[:, :largura] = imagem_colorida
    resultado[:, largura:] = cv2.cvtColor(imagem_em_tons_de_cinza, cv2.COLOR_GRAY2BGR)

    cv2.imshow('Imagem Colorida e em Tons de Cinza', resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()