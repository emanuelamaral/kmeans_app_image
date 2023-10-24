import os
import cv2
from src.features.kmeans import GeneratedKmeans


class KmeansViewAndGenerate:
    def __init__(self, original_image, var_dimensions, var_clusters):
        self.original_image = original_image
        self.var_dimensions = var_dimensions
        self.var_clusters = var_clusters

    # Gera as telas a partir das imagens salvas no diretório ../images/saved_images/
    @staticmethod
    def kmeans_view():
        saved_images_dir = '../images/saved_images/'
        image_files = os.listdir(saved_images_dir)
        image_files = [os.path.join(saved_images_dir, file) for file in image_files if file.endswith('.jpg')]

        for image_file in image_files:
            image = cv2.imread(image_file)

            if image is not None:
                cv2.namedWindow(os.path.basename(image_file), cv2.WINDOW_NORMAL)
                cv2.imshow(os.path.basename(image_file), image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Gerar kmeans com os valores do cluster, e dimensão da imagem
    def generate_kmeans(self):
        GeneratedKmeans(self.original_image, self.var_dimensions.get(), self.var_clusters.get())