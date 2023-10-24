import tkinter as tk
from config_file_frame import ConfigFileFrame
from src.features.kmeans_view_and_generate import KmeansViewAndGenerate


class ConfigFrame:
    def __init__(self, master):

        self.master = master

        self.bottons_frame_buttons = None
        self.top_frame_buttons = None
        self.button_load_image = None
        self.dropdown_button_cluster = None
        self.dropdown_button_dimension = None
        self.button_generate_kmeans_button = None
        self.button_view_kmeans_result_images = None

        self.frame_image = None

        self.var_dimensions = None
        self.var_clusters = None

        self.kmeansViewAndGenerate = None

        self.config_frame()

    # Configuração geral do frame
    def config_frame(self):
        self.master.title("Kmeans App Image")
        self.master.geometry("720x720")
        self.config_top_frame_buttons()
        self.config_frame_image()
        self.config_bottom_frame_buttons()

    # Configura o frame da imagem que fica centralizado
    def config_frame_image(self):
        self.frame_image = tk.Frame(self.master)
        self.frame_image.pack(side="top", expand=True, fill="both")

    # Configura o frame dos botões da parte de baixo
    def config_bottom_frame_buttons(self):
        self.bottons_frame_buttons = tk.Frame(self.master)
        self.bottons_frame_buttons.pack(side="bottom", pady=10)

        self.button_load_image = tk.Button(self.bottons_frame_buttons, text="Carregar imagem", command=self.open_file)
        self.button_load_image.pack(side="left", padx=10)

        self.button_generate_kmeans_button = tk.Button(self.bottons_frame_buttons, text="Gerar Kmeans",
                                                       command=self.generate_kmeans, state="disabled")
        self.button_generate_kmeans_button.pack(side="left", padx=10)

        self.button_view_kmeans_result_images = tk.Button(self.bottons_frame_buttons, text="Visualizar Kmeans",
                                                          command=self.kmeans_view, state="disabled")
        self.button_view_kmeans_result_images.pack(side="left", padx=10)

    # Configura o frame dos botões da parte de cima
    def config_top_frame_buttons(self):
        self.top_frame_buttons = tk.Frame(self.master)
        self.top_frame_buttons.pack(side="top", pady=10)

        clusters = ["K = 1", "K = 2", "K = 3", "K = 4", "K = 5", "K = 6", "K = 7", "K = 8", "K = 9", "K = 10"]
        image_dimensions = ["D = 1", "D = 2", "D = 3"]

        # Configuração do combobox/dropdown button da dimensão da imagem
        label_dimensions = tk.Label(self.top_frame_buttons, text="Selecionar dimensão da imagem:")
        label_dimensions.pack(side="left")
        self.var_dimensions = tk.StringVar(self.master)
        self.var_dimensions.set("D = 3")
        self.dropdown_button_dimension = tk.OptionMenu(self.top_frame_buttons, self.var_dimensions, *image_dimensions)
        self.dropdown_button_dimension.pack(side="left", padx=10)

        # Configuração do combobox/drodown button do número de K
        label_clusters = tk.Label(self.top_frame_buttons, text="Selecionar K:")
        label_clusters.pack(side="left")
        self.var_clusters = tk.StringVar(self.master)
        self.var_clusters.set("K = 4")
        self.dropdown_button_cluster = tk.OptionMenu(self.top_frame_buttons, self.var_clusters, *clusters)
        self.dropdown_button_cluster.pack(side="left", padx=10)

    def open_file(self):
        config_file_frame = ConfigFileFrame(self.frame_image)

        config_file_frame.open_file()
        self.kmeansViewAndGenerate = KmeansViewAndGenerate(config_file_frame.original_image, self.var_dimensions,
                                                           self.var_clusters)

        self.button_generate_kmeans_button["state"] = "normal"
        self.button_view_kmeans_result_images["state"] = "normal"

    def generate_kmeans(self):
        self.kmeansViewAndGenerate.generate_kmeans()

    def kmeans_view(self):
        self.kmeansViewAndGenerate.kmeans_view()
