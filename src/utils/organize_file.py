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
    for filename in os.listdir(initial_path):
        name, type = os.path.splitext(filename)

        if not os.path.exists(f'{final_path}\{type}'):
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
