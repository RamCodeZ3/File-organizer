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

# home = os.path.expanduser("~")
# downloads_path = os.path.join(home, "Downloads")
# document_path = os.path.join(home, "Documents\Prueba de archivos organizado")

# for filename in os.listdir(downloads_path):
#     name, type = os.path.splitext(filename)
    
#     if not os.path.exists(f'{document_path}\{type}'):
#         new_dir = type.replace('.', '').capitalize()
#         Path(f'{document_path}\{new_dir}').mkdir(exist_ok=True)
#         shutil.move(f"{downloads_path}\{filename}", f"{document_path}\{new_dir}")
    
#     else:
#        shutil.move(f"{downloads_path}\{filename}", f"{document_path}\{new_dir}")


# if __name__ == '__main__':
#     print('ruta:',downloads_path)