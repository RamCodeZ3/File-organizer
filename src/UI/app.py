import customtkinter as ctk
from utils.organize_file import get_folded_path, organize_files


class App:
    def __init__(self):
        self.initial_path = None
        self.final_path = None
        self.create_ui()

    def create_ui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()
        self.app.title("Organizador de Archivos")
        self.app.geometry("520x200")
        self.app.resizable(False, False)

        MAIN_COLOR = "#3660E7"

        self.btn_origen = ctk.CTkButton(
            self.app,
            text="Seleccionar carpeta de origen",
            command=self.set_initial_path,
            fg_color=MAIN_COLOR,
            hover_color="#4A75FF",
            text_color="white",
            corner_radius=10,
            width=200
        )
        self.btn_origen.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.label_origen = ctk.CTkLabel(
            self.app,
            text="Ruta no seleccionada",
            text_color=MAIN_COLOR,
            anchor="w"
        )
        self.label_origen.grid(row=0, column=1, padx=10, sticky="w")

        self.btn_destino = ctk.CTkButton(
            self.app,
            text="Seleccionar carpeta de destino",
            command=self.set_final_path,
            fg_color=MAIN_COLOR,
            hover_color="#4A75FF",
            text_color="white",
            corner_radius=10,
            width=200
        )
        self.btn_destino.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.label_destino = ctk.CTkLabel(
            self.app,
            text="Ruta no seleccionada",
            text_color=MAIN_COLOR,
            anchor="w"
        )
        self.label_destino.grid(row=1, column=1, padx=10, sticky="w")

        self.btn_organizar = ctk.CTkButton(
            self.app,
            text="Organizar Archivos",
            command=self.handle_organize_files,
            fg_color=MAIN_COLOR,
            hover_color="#4A75FF",
            text_color="white",
            corner_radius=10,
            width=400,
            height=40
        )
        self.btn_organizar.grid(row=2, column=0, columnspan=2, pady=(20, 10))

        self.label_status = ctk.CTkLabel(
            self.app,
            text="",
            text_color="#FF5555",
            anchor="center"
        )
        self.label_status.grid(row=3, column=0, columnspan=2, pady=(5, 0))

        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_columnconfigure(1, weight=2)

        self.app.mainloop()

    def handle_organize_files(self):
        try:
            result = organize_files(self.initial_path, self.final_path)

            if isinstance(result, dict):
                if result.get("success"):
                    self.label_status.configure(
                        text="Archivos organizados correctamente",
                        text_color="#4AE77E"
                    )
                else:
                    self.label_status.configure(
                        text=f"Error: {
                            result.get('error', 'Error desconocido')
                        }",
                        text_color="#FF5555"
                    )
            else:
                self.label_status.configure(
                    text="Organización completada",
                    text_color="#4AE77E"
                )

        except Exception as e:
            self.label_status.configure(
                text=f"Error inesperado: {str(e)}",
                text_color="#FF5555"
            )

    def set_initial_path(self):
        self.initial_path = get_folded_path()
        if self.initial_path:
            self.label_origen.configure(text=self.initial_path)

    def set_final_path(self):
        self.final_path = get_folded_path()
        if self.final_path:
            self.label_destino.configure(text=self.final_path)


if __name__ == "__main__":
    App()
