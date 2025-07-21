import os, shutil, tempfile, ctypes, errno

def archivoEnUso(exc):
    return hasattr(exc, 'winerror') and exc.winerror == 32


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
            except PermissionError as e:
                if(archivoEnUso(e)):
                    print("Archivo en uso (Omitido): ", archivo)
                else:
                    print("Archivo con permiso denegado: ", archivo)
        
        for nombre in directorios:
            carpeta = os.path.join(root,nombre)
            try:
                #os.rmdir(carpeta)
                print("Carpeta eliminada: ", carpeta)
            except Exception as e:
                print("Carpeta con permiso denegado: ",carpeta)
             


if __name__ == "__main__":
    borrarTemporales()