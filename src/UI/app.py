import tkinter as tk
from utils.organize_file import get_folded_path, organize_files

class App:
    def __init__(self):
        self.type = None
        self.initial_path = None
        self.final_path = None
        self.app_ui()

    def app_ui(self):
        app = tk.Tk()
        app.title("Organizador de archivos")
        app.geometry("350x250")
        app.resizable(height=False, width=False)
        app.config(bg="#232323")

        button_file_dialog = tk.Button(
            app, 
            text="Selecciona la carpeta de origen", 
            bg="blue", 
            bd=0,
            fg="white",
            font=("Arial", 12),
            command=lambda: self.set_initial_path()
        )
        
        button_file_dialog_2 = tk.Button(
            app, 
            text="Selecciona la carpeta final", 
            bg="blue", 
            bd=0,
            fg="white",
            font=("Arial", 12),
            command=lambda: self.set_final_path()
        )

        button_organize_file = tk.Button(
            app, 
            text="Organizar archivos", 
            bg="blue", 
            bd=0,
            fg="white",
            font=("Arial", 12),
            command=lambda: organize_files(self.initial_path, self.final_path)
        )

        button_file_dialog.pack(pady=20)
        button_file_dialog_2.pack(pady=20)
        button_organize_file.pack(pady=20)

        app.mainloop()
    
    def set_initial_path(self):
        self.initial_path = get_folded_path()
    
    def set_final_path(self):
        self.final_path = get_folded_path()