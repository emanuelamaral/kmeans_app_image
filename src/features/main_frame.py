import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import cv2
from PIL import Image, ImageTk


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

        self.image_path = None
        self.original_image = None
        self.label_original_image = None

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
        self.button_load_image.pack(side="top", padx=10)

    def config_top_frame_buttons(self):
        self.top_frame_buttons = tk.Frame(self.master)
        self.top_frame_buttons.pack(side="top", pady=10)

        clusters = ["K = 1", "K = 2", "K = 3", "K = 4", "K = 5", "K = 6", "K = 7", "K = 8", "K = 9", "K = 10"]
        image_dimensions = ["D = 1", "D = 2", "D = 3", "D = 4", "D = 5", "D = 6", "D = 7", "D = 8", "D = 9", "D = 10"]

        label_dimensions = tk.Label(self.top_frame_buttons, text="Selecionar dimensão da imagem:")
        label_dimensions.pack(side="left")

        var_dimensions = tk.StringVar(self.master)
        var_dimensions.set("D = 4")

        self.dropdown_button_dimension = tk.OptionMenu(self.top_frame_buttons, var_dimensions, *image_dimensions)
        self.dropdown_button_dimension.pack(side="left", padx=10)

        label_clusters = tk.Label(self.top_frame_buttons, text="Selecionar K:")
        label_clusters.pack(side="left")

        var_clusters = tk.StringVar(self.master)
        var_clusters.set("K = 4")

        self.dropdown_button_cluster = tk.OptionMenu(self.top_frame_buttons, var_clusters, *clusters)
        self.dropdown_button_cluster.pack(side="left", padx=10)

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
        cv2.destroyAllWindows()
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = KmeansAppFrame(root)
    app.run()
