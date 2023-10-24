import tkinter as tk
from config_frame import ConfigFrame


class KmeansAppFrame:
    def __init__(self, master):
        self.master = master

        self.init_app()

    # Configura o frame geral
    def init_app(self):
        ConfigFrame(self.master)

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = KmeansAppFrame(root)
    app.run()
