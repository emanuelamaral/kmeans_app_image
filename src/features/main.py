import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('../images/car1.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, channels = image.shape

# Converter a imagem para um array unidimensional de pixels
pixels = image.reshape((-1, 3)).astype(np.float32)

# Número de clusters (K)
MAX_K = 10

K = 8

if K <= MAX_K:
    for k in range(1, K + 1):
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Converter os centróides de volta para valores inteiros
        centers = np.uint8(centers)

        # Atribuir a cada pixel o centróide mais próximo
        segmented_image = centers[labels.flatten()]

        # Redimensionar a imagem segmentada de volta para a forma original
        segmented_image = segmented_image.reshape(image.shape)

        if k > 1:
            cv2.namedWindow(f'Imagem com valor de K={k}', cv2.WINDOW_NORMAL)

            # Mostrar a imagem segmentada com valor de K correspondente
            cv2.imshow(f'Imagem com valor de K={k}', segmented_image)
            key = cv2.waitKey(0)  # Esperar por uma tecla pressionada
            if key == ord('q'):  # Pressionar 'q' para fechar a janela
                break
            else:
                continue


cv2.namedWindow('Imagem Original', cv2.WINDOW_NORMAL)
# Mostrar a imagem original
cv2.imshow('Imagem Original', image)
cv2.waitKey(0)

# Fechar todas as janelas
cv2.destroyAllWindows()
