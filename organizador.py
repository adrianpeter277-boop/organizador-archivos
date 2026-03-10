import os
import shutil

categorias = {
    "Imagenes":  [".jpg",".jpeg",".png",".gif",".svg"],
    "Videos":    [".mp4",".mov",".avi",".mkv"],
    "PDFs":      [".pdf"],
    "Musica":    [".mp3",".wav","flac"],
    "Documentos":[".doc",".docx",".txt",".xlsx"],
    "Otros":     []
}

def organizar(carpeta):
    for archivo in os.listdir(carpeta):
        ruta = os.path.join(carpeta, archivo)

        #Saltamos si es una carpeta
        if os.path.isdir(ruta):
            continue

        #Obtenemos la extension
        _, extension = os.path.splitext(archivo)

        #Buscar a que categoria pertenece
        destino = "Otros"
        for categoria, extensiones in categorias.items():
            if extension.lower() in extensiones:
                destino = categoria
                break

        #Crear la carpeta destino si no existe
        carpeta_destino = os.path.join(carpeta, destino)
        os.makedirs(carpeta_destino, exist_ok=True)

        #Mover el archivo
        shutil.move(ruta, os.path.join(carpeta_destino, archivo))
        print(f"Movido: {archivo} > {destino}/")

carpeta = input("¿Que carpeta quieres organizar?")
organizar(carpeta)
print("¡Listo! Carpeta organizada")