import os 
import datetime
import zipfile


def crear_nombre_backup():
    """Genera un nombre para el archivo de backup basado en la fecha y hora actual"""
    fecha_hora =datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"backup_{fecha_hora}.zip"

def crear_backup(carpeta_origen,carpeta_destino):
    """
    Crea un archivo ZIP con el contenido de la carpeta origen
    
    Args:
        carpeta_origen  : Ruta de la carpeta de respaldar
        carpeta_destino : Ruta donde se guardara el archivo de backup
    
    Returns:
        str:Ruta completa del archivo de backup 
    """
    if not os.path.exists(carpeta_origen):
        print(f"Error: La carpeta de origen '{carpeta_origen}' no existe.")
        return None

    if not os.path.exists(carpeta_destino):
        print(f"Creando carpeta de destino '{carpeta_destino}'...")
        os.makedirs(carpeta_destino)

    # Crear nombre del archivo de backup
    nombre_backup = crear_nombre_backup()
    ruta_backup = os.path.join(carpeta_destino, nombre_backup)