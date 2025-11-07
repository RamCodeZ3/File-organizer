import tkinter as tk
from utils.organize_file import get_initial_route

class App:
    def __init__(self):
        self.type = None
        self.initial_route = None
        self.final_route = None

    def app_ui(self):
        app = tk.Tk()
        app.title("Organizador de archivos")
        app.geometry("350x250")
        app.resizable(height=False, width=False)

        button_file_dialog = tk.Button(
            app, 
            text="Selecciona la carpeta de origen", 
            bg="blue", 
            bd=0,
            fg="white",
            font=("Arial", 12)
        )
        button_file_dialog.pack(pady=20)

        app.mainloop()
