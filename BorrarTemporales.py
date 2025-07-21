import os, shutil, tempfile


def borrarTemporales(directorio=None):
    if directorio is None:
        directorio = tempfile.gettempdir()
        print(directorio)
    
    for root, directorios, archivos in os.walk(directorio, topdown=False):
        for nombre in archivos:
            archivo = os.path.join(root,nombre)
            try:
                #os.remove(archivo)
                print("Archivo eliminado: ", archivo)
            except Exception as e:
                print("Error: ", e)
        
        for nombre in directorios:
            carpeta = os.path.join(root,nombre)
            try:
                #os.rmdir(carpeta)
                print("Carpeta eliminada: ", carpeta)
            except Exception as e:
                print("Error: ",e)
             


if __name__ == "__main__":
    borrarTemporales()