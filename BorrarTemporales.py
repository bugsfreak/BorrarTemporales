import os, shutil, tempfile, errno

def archivoEnUso(exc):
    return hasattr(exc, 'winerror') and exc.winerror == 32


def borrarTemporales(directorio=None, logger=print):
    if directorio is None:
        directorio = tempfile.gettempdir()
        print(directorio)
        
    logger(f"\nLimpieza de archivos temporales en: {directorio}\n")
    
    for root, directorios, archivos in os.walk(directorio, topdown=False):
        for nombre in archivos:
            archivo = os.path.join(root,nombre)
            try:
                #os.remove(archivo)
                logger(f"Archivo eliminado: {archivo}")
            except PermissionError as e:
                if(archivoEnUso(e)):
                    logger(f"Archivo en uso (Omitido): {archivo}")
                else:
                    logger(f"Archivo con permiso denegado: {archivo}")
        
        for nombre in directorios:
            carpeta = os.path.join(root,nombre)
            try:
                #os.rmdir(carpeta)
                logger(f"Carpeta eliminada: {carpeta}")
            except Exception as e:
                logger(f"Carpeta con permiso denegado: {carpeta}")
             