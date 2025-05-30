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
        carpeta_origen  : Ruta de la carpeta de respaldar: 
        carpeta_destino : Ruta donde se guardara el archivo de backup:
    
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
    
    
    # Crear archivo ZIP
    print(f"Creando backup en '{ruta_backup}'...")

    with zipfile.ZipFile(ruta_backup, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Recorrer todos los archivos y carpetas en la carpeta de origen
        for carpeta_actual, subcarpetas, archivos in os.walk(carpeta_origen):
            for archivo in archivos:
                ruta_archivo = os.path.join(carpeta_actual, archivo)
                # Guardar la ruta relativa en el ZIP
                ruta_relativa = os.path.relpath(ruta_archivo, os.path.dirname(carpeta_origen))
                zip_file.write(ruta_archivo, ruta_relativa)
                print(f"Añadido: {ruta_relativa}")
    print(f'backup completado:{ruta_backup}')
    return ruta_backup
    

def main ():
    """Funcion principal del programa"""
    print("===BACKUP AUTAMTICO===")
    
    #Configuracion de carpetas (puedes modificar las rutas que sea necesaria)
    carpeta_origen = input ("Ingresa la ruta de la carpeta a respaldar : ")
    carpeta_destino = input("Ingresa la ruta donde guardar el backup (deja en blanco para usar './backup'):")
    
    if not carpeta_destino :
        carpeta_destino ="./backup"
    
    #crea backup
    ruta_backup = crear_backup(carpeta_origen,carpeta_destino)
    
    if ruta_backup :
        print(f"\nTamaño del backup:{os.path.getsize(ruta_backup)/(1024*1024):.2f}MB")
        print("\n!Backup completado con exito")
        
if __name__=="__main__":
    main()