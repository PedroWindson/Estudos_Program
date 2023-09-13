import cv2

# Insira o diretório onde as imagens estão armazenadas
imagem = cv2.imread('C:\\Users\\karat\\Downloads\\image.jpg') # Deixei as imagens em meu computador, pois dava bug toda vez que eu mudava elas de diretório.

if imagem is None:
    print("Não foi possível carregar a imagem.")
else:
    imagem_suavizada_media = cv2.blur(imagem, (9, 5))

    imagem_suavizada_gaussiano = cv2.GaussianBlur(imagem, (5, 5), 5)  # Tamanho do kernel: (5, 5); Desvio padrão: (0).

    # Isso mostra a imagem original
    cv2.imshow('Imagem Original', imagem)

    # Isso mostra a imagem suavizada com filtro de média
    cv2.imshow('Imagem Suavizada (Média)', imagem_suavizada_media)

    # Isso mostra a imagem suavizada com filtro Gaussiano
    cv2.imshow('Imagem Suavizada (Gaussiano)', imagem_suavizada_gaussiano)

    cv2.waitKey(0)
    cv2.destroyAllWindows()