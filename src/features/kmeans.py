import cv2
import numpy as np
import os
import shutil


class GeneratedKmeans:
    def __init__(self, original_image, dim_images, k_value):
        # Número de clusters (K)
        self.MAX_K = 10

        self.dim_images = dim_images
        self.K = k_value

        self.config_values()

        # Carregar a imagem
        # self.image = cv2.cvtColor(original_image.copy(), cv2.COLOR_BGR2RGB)
        self.image = original_image.copy()
        self.height, self.width, self.channels = self.image.shape

        # Converter a imagem para um array unidimensional de pixels
        self.pixels = self.image.reshape((-1, self.dim_images)).astype(np.float32)

        self.run()

    def config_values(self):
        if self.K == "K = 1":
            self.K = 1
        elif self.K == "K = 2":
            self.K = 2
        elif self.K == "K = 3":
            self.K = 3
        elif self.K == "K = 4":
            self.K = 4
        elif self.K == "K = 5":
            self.K = 5
        elif self.K == "K = 6":
            self.K = 6
        elif self.K == "K = 7":
            self.K = 7
        elif self.K == "K = 8":
            self.K = 8
        elif self.K == "K = 9":
            self.K = 9
        elif self.K == "K = 10":
            self.K = 10

        if self.dim_images == "D = 1":
            self.dim_images = 1
        elif self.dim_images == "D = 2":
            self.dim_images = 2
        elif self.dim_images == "D = 3":
            self.dim_images = 3

    def run(self):
        # Certifique-se de que o diretório 'saved-images' exista

        if os.path.exists('../images/saved_images'):
            shutil.rmtree('../images/saved_images')

        if not os.path.exists('../images/saved_images'):
            os.makedirs('../images/saved_images')

        for k in range(1, self.K + 1):
            stop_criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 500, 0.10)
            _, labels, centers = cv2.kmeans(self.pixels, k, None, stop_criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

            # Converter os centróides de volta para valores inteiros
            centers = np.uint8(centers)

            # Atribuir a cada pixel o centróide mais próximo
            segmented_image = centers[labels.flatten()]

            # Redimensionar a imagem segmentada de volta para a forma original
            segmented_image = segmented_image.reshape(self.image.shape)

            # Salvar a imagem segmentada com valor de K correspondente no diretório 'saved-images'
            output_filename = os.path.join('../images/saved_images', f'segmented_image_k_{k}.jpg')
            cv2.imwrite(output_filename, segmented_image)
            print(f'Imagem com valor de K={k} salva como {output_filename}')

        cv2.destroyAllWindows()  # Fecha todas as janelas do OpenCV
