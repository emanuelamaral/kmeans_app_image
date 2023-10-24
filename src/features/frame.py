import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
from kmeans import GeneratedKmeans
import os
import matplotlib.pyplot as plt


class KmeansAppFrame:
    def __init__(self, master):
        self.master = master

        self.label_image = None
        self.frame_image = None

        self.bottons_frame_buttons = None
        self.top_frame_buttons = None

        self.button_load_image = None
        self.dropdown_button_cluster = None
        self.dropdown_button_dimension = None
        self.button_generate_kmeans_button = None
        self.button_view_kmeans_result_images = None

        self.image_path = None
        self.original_image = None
        self.label_original_image = None

        self.var_dimensions = None
        self.var_clusters = None

        self.config_frame()

    def config_frame(self):
        self.master.title("Kmeans App Image")
        self.master.geometry("720x720")
        self.config_top_frame_buttons()
        self.config_frame_image()
        self.config_bottom_frame_buttons()

    def config_frame_image(self):
        self.frame_image = tk.Frame(self.master)
        self.frame_image.pack(side="top", expand=True, fill="both")

    def config_bottom_frame_buttons(self):
        self.bottons_frame_buttons = tk.Frame(self.master)
        self.bottons_frame_buttons.pack(side="bottom", pady=10)

        self.button_load_image = tk.Button(self.bottons_frame_buttons, text="Carregar imagem", command=self.open_file)
        self.button_load_image.pack(side="left", padx=10)

        self.button_generate_kmeans_button = tk.Button(self.bottons_frame_buttons, text="Gerar Kmeans", command=self.generate_kmeans)
        self.button_generate_kmeans_button.pack(side="left", padx=10)

        self.button_view_kmeans_result_images = tk.Button(self.bottons_frame_buttons, text="Visualizar Kmeans", command=self.kmeans_view)
        self.button_view_kmeans_result_images.pack(side="left", padx=10)

    def config_top_frame_buttons(self):
        self.top_frame_buttons = tk.Frame(self.master)
        self.top_frame_buttons.pack(side="top", pady=10)

        clusters = ["K = 1", "K = 2", "K = 3", "K = 4", "K = 5", "K = 6", "K = 7", "K = 8", "K = 9", "K = 10"]
        image_dimensions = ["D = 1", "D = 2", "D = 3"]

        label_dimensions = tk.Label(self.top_frame_buttons, text="Selecionar dimensão da imagem:")
        label_dimensions.pack(side="left")

        self.var_dimensions = tk.StringVar(self.master)
        self.var_dimensions.set("D = 3")

        self.dropdown_button_dimension = tk.OptionMenu(self.top_frame_buttons, self.var_dimensions, *image_dimensions)
        self.dropdown_button_dimension.pack(side="left", padx=10)

        label_clusters = tk.Label(self.top_frame_buttons, text="Selecionar K:")
        label_clusters.pack(side="left")

        self.var_clusters = tk.StringVar(self.master)
        self.var_clusters.set("K = 4")

        self.dropdown_button_cluster = tk.OptionMenu(self.top_frame_buttons, self.var_clusters, *clusters)
        self.dropdown_button_cluster.pack(side="left", padx=10)

    def kmeans_view(self):
        saved_images_dir = '../images/saved_images/'
        image_files = os.listdir(saved_images_dir)
        image_files = [os.path.join(saved_images_dir, file) for file in image_files if file.endswith('.jpg')]

        for image_file in image_files:
            # Lê a imagem usando OpenCV
            image = cv2.imread(image_file)

            if image is not None:
                # Exibe a imagem em uma janela com o nome do arquivo
                cv2.namedWindow(os.path.basename(image_file), cv2.WINDOW_NORMAL)
                cv2.imshow(os.path.basename(image_file), image)

            # Aguarda até que uma tecla seja pressionada e, em seguida, fecha todas as janelas
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def generate_kmeans(self):
        GeneratedKmeans(self.original_image, self.var_dimensions.get(), self.var_clusters.get())

    def open_file(self):
        self.image_path = filedialog.askopenfilename()

        if self.image_path:
            print("Arquivo Selecionado", self.image_path)
            self.load_image()
        else:
            print("Nenhum arquivo selecionado")

    def load_image(self):
        self.original_image = cv2.imread(self.image_path)
        self.show_original_image(self.original_image.copy())

    def show_original_image(self, img):
        if self.label_original_image:
            self.label_original_image.destroy()

        image_width = 650
        image_height = 500
        resized_image = cv2.resize(img, (image_width, image_height))

        resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

        pil_image = Image.fromarray(resized_image_rgb)
        tk_image = ImageTk.PhotoImage(image=pil_image)

        self.label_original_image = tk.Label(self.frame_image, image=tk_image)
        self.label_original_image.image = tk_image
        self.label_original_image.pack(expand=True, fill="both")

        self.frame_image.update_idletasks()

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = KmeansAppFrame(root)
    app.run()
