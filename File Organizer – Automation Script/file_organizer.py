import os
import shutil

BASE_PATH = "C:/Users/fenno/OneDrive/Escritorio/example"

EXTENSION_FOLDERS = {
    ".mp4": "mp4",
    ".txt": "txt",
    ".png": "png",
    ".jpg": "jpg",
    ".py": "python",
    ".csv": "csv",
    ".yml": "yml"
}

for archivo in os.listdir(BASE_PATH):
    archivo_path = os.path.join(BASE_PATH, archivo)

    if not os.path.isfile(archivo_path):
        continue

    _, extension = os.path.splitext(archivo)
    extension = extension.lower()

    if extension in EXTENSION_FOLDERS:
        carpeta_destino = os.path.join(BASE_PATH, EXTENSION_FOLDERS[extension])

        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        shutil.move(archivo_path, os.path.join(carpeta_destino, archivo))
