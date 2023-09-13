import cv2

# Insira o diretório onde as imagens estão armazenadas
imagem = cv2.imread('C:\\Users\\karat\\Downloads\\A.jpg') # Deixei as imagens em meu computador, pois dava bug toda vez que eu mudava elas de diretório.

# Verificando se deu certo
if imagem is None:
    print("Não foi possível carregar a imagem.")
else:
    cv2.imshow('Imagem', imagem)

    cv2.waitKey(0)
    cv2.destroyAllWindows()