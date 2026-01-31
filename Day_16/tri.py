from pathlib import Path

dirs = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".flac": "Musique",

    ".avi": "Videos",
    ".mp4": "Videos",
    ".gif": "Videos",

    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",

    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents",
    ".pdf": "Documents",
    ".doc": "Documents"

}

from pathlib import Path


path_dir = Path(input("Input directory path: "))

files = [f for f in path_dir.iterdir() if f.is_file()]
for f in files:
    # Si aucune correspondance n'est trouvé pour l'extension, on place les fichiers dans un dossier Autres
    output_dir = path_dir / dirs.get(f.suffix, "Divers")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)

print(files)