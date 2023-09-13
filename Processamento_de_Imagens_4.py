import cv2

# Insira o diretório onde as imagens estão armazenadas
imagem_em_tons_de_cinza = cv2.imread('C:\\Users\\karat\\Downloads\\A.jpg', cv2.IMREAD_GRAYSCALE) # Deixei as imagens em meu computador, pois dava bug toda vez que eu mudava elas de diretório.

if imagem_em_tons_de_cinza is None:
    print("Não foi possível carregar a imagem em tons de cinza.")
else:
    # Isso aplica o operador de detecção de bordas (nesse caso, o operador de Sobel)
    bordas = cv2.Sobel(imagem_em_tons_de_cinza, cv2.CV_64F, 1, 0, ksize=3)  # Operador de Sobel para detecção de bordas horizontais

    # Isso converte as bordas de volta para uma imagem em tons de cinza com escala de cinza
    bordas = cv2.convertScaleAbs(bordas)

    # Isso mostra a imagem de bordas resultante
    cv2.imshow('Imagem de Bordas', bordas)

    cv2.waitKey(0)
    cv2.destroyAllWindows()