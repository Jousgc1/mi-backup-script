import os
import shutil
from datetime import datetime


fecha = datetime.now().strftime("%Y-%m-%d")
nueva_carpeta = f"Backup_{fecha}"


#Crea una carpeta si en caso no exista
if not os.path.exists(nueva_carpeta):
    os.makedirs(nueva_carpeta)
    print(f"Backup '{nueva_carpeta}'creada.")
    
carpeta_origen ="C:\\Users\\USER\\Desktop\\python\\archivo"
    
contador = 0
    
for archivo in os.listdir(carpeta_origen):
    if archivo.endswith(".txt"):
        origen = os.path.join(carpeta_origen,archivo)
        destino =os.path.join(nueva_carpeta,archivo)
        shutil.move(origen,destino)
        print(origen)
        contador +=1
    
print(f"Backup '{contador}'archivos a la carpeta'{nueva_carpeta}' .")
        
