from dotenv import load_dotenv
import os
from cryptography.fernet import Fernet
from outlook_reader import * #obtener_transacciones
from excel_writer import * #guardar_transacciones_excel
from notion_conn import * #sincronizar_notion

# Cargar variables de entorno
def cargar_config():
    load_dotenv()
    with open("secret.key", "rb") as f:
        key = f.read()
    fernet = Fernet(key)
    return {
        'EMAIL': os.getenv("EMAIL"),
        'PASSWORD': fernet.decrypt(os.getenv("PASSWORD_MAIL").encode()).decode(),
        'EXCEL_PATH': os.getenv("EXCEL_PATH"),
        'HOJA_EXCEL': os.getenv("HOJA_EXCEL"),
        'NOTION_TOKEN': fernet.decrypt(os.getenv("NOTION_TOKEN").encode()).decode(),
        'NOTION_DATABASE_ID': os.getenv("NOTION_DATABASE_ID")
    }

def main():
    config = cargar_config()
    print("🔑 Configuración cargada.")

#     transacciones = obtener_transacciones(config['EMAIL'], config['PASSWORD'])

#     if transacciones:
#         guardar_transacciones_excel(config['EXCEL_PATH'], config['HOJA_EXCEL'], transacciones)
#         sincronizar_notion(config['NOTION_TOKEN'], config['NOTION_DATABASE_ID'], transacciones)
#     else:
#         print("📭 No se encontraron nuevas transacciones.")

if __name__ == "__main__":
    main()