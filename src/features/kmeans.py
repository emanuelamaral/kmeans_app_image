import cv2
import numpy as np
import os
import shutil


class GeneratedKmeans:
    def __init__(self, original_image, dim_images, k_value):
        # número máximo de clusters
        self.K = k_value
        self.MAX_K = 10

        # Configurações dos valores
        self.dim_images = dim_images
        self.K = k_value
        self.config_values()

        # configurando a imagem e pegando os valores do shape
        self.image = original_image.copy()
        self.height, self.width, self.channels = self.image.shape

        # pega os pixels da imagem
        self.pixels = self.image.reshape((-1, self.dim_images)).astype(np.float32)

        self.run()

    # Configura os valores de K e da dimensão da imagem
    def config_values(self):
        for i in range(1, 11):
            if self.K == f"K = {i}":
                self.K = i

        for i in range(1, 4):
            if self.dim_images == f"D = {i}":
                self.dim_images = i

    def run(self):

        # se já possui arquivo criado, deleta para criar outro
        if os.path.exists('../images/saved_images'):
            shutil.rmtree('../images/saved_images')

        os.makedirs('../images/saved_images')

        for k in range(1, self.K + 1):
            # cria o critério de parada
            # número máximo de iterações (100) ou alteração nas médias dos clusters menor que 0.2
            stopping_criterion = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
            _, labels, centers = cv2.kmeans(self.pixels, k, None, stopping_criterion, 10, cv2.KMEANS_RANDOM_CENTERS)
            
            # trunca os valores para inteiro
            centers = np.uint8(centers)
            
            # pega a imagem de acordo com a classificação e reconfigura a imagem com o tamanho original
            segmented_image = centers[labels.flatten()]
            segmented_image = segmented_image.reshape(self.image.shape)

            # Salva imagens no diretório criado 
            output_filename = os.path.join('../images/saved_images', f'segmented_image_k_{k}.jpg')
            cv2.imwrite(output_filename, segmented_image)
            print(f'Imagem com valor de K={k} salva como {output_filename}')

        cv2.destroyAllWindows()
