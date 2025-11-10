import os
import shutil
from pathlib import Path
from tkinter import filedialog


def get_folded_path():
    folder_path = filedialog.askdirectory()
    if folder_path:
        return folder_path
    else:
        return None

def organize_files(initial_path, final_path):
      try:
           for filename in os.listdir(initial_path):
            source = os.path.join(initial_path, filename)
            name, type = os.path.splitext(filename)

            if os.path.isdir(source):
                continue

            if not os.path.exists(f'{final_path}\{type}') and type != '.ini':
                new_folder = type.replace('.', '').upper()
                Path(f'{final_path}\{new_folder}').mkdir(exist_ok=True)
                shutil.move( 
                    f"{initial_path}\{filename}",
                    f"{final_path}\{new_folder}"
                )

            else:
                shutil.move(
                    f"{initial_path}\{filename}",
                    f"{final_path}\{new_folder}"
                )
      
      except TypeError as e: 
          return {"success": False, "error": "No se encontró la carpeta origen"}
