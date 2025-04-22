from dotenv import load_dotenv
import os
import sys
from read_excel import read_excel_file
from notion_conn import create_notion_page
import datetime

def vars_env():
    ENV_PATH = "list.env"
    try:
        with open(ENV_PATH, 'r') as f:
            pass  # Solo para verificar que el archivo existe
    except FileNotFoundError:
        print(f"❌ Error: el archivo {ENV_PATH} no se encontró.")
        sys.exit(1)

    load_dotenv(dotenv_path="list.env")

    try:
        NOTION_TOKEN = os.getenv("NOTION_TK")
        NOTION_DATABASE_ID = os.getenv("NOTION_DB")
        EXCEL_FILE_PATH = os.getenv("EXC_PATH")
        EXCEL_SHEET_NAME = os.getenv("EXC_PG")
    except KeyError as e:
        print(f"❌ Error: la variable de entorno {e} no está definida.")
        sys.exit(1)

    print("✅ Variables cargadas correctamente.")
    return NOTION_TOKEN, NOTION_DATABASE_ID, EXCEL_FILE_PATH, EXCEL_SHEET_NAME

def main():
    NOTION_TOKEN, NOTION_DATABASE_ID, EXCEL_FILE_PATH, EXCEL_SHEET_NAME = vars_env()

    datos_excel = read_excel_file(EXCEL_FILE_PATH, EXCEL_SHEET_NAME)
    if datos_excel is None:
        print("❌ Error: no se pudieron leer los datos del archivo Excel.")
        sys.exit(1)
    for fila in datos_excel:
        fecha = fila[6]  # Cambia el índice según la columna que necesites
        if not isinstance(fecha,(datetime.date, datetime.datetime)):
            fecha_fin = datetime.datetime.strptime(fila[6], "%Y-%m-%d")
        else:
            fecha_fin = str(fecha) # Cambia el formato según sea necesario
        # Aquí puedes definir las propiedades que deseas enviar a Notion
        properties = {
            "Nombre": {
                "title": [
                    {
                        "text": {
                            "content": str(fila[5])
                        }
                    }
                ]
            },
            "Fecha": {
                "date":{
                        "start":fecha_fin
                    }
            }
        }
        if not create_notion_page(NOTION_TOKEN, NOTION_DATABASE_ID, properties):
            print("❌ Error: no se pudo crear la página en Notion.")
            sys.exit(1)

    # Aquí puedes llamar a otras funciones o clases que necesiten estas variables
    # Por ejemplo:
    # from src.notion import Notion
    # notion = Notion(NOTION_TOKEN, NOTION_DATABASE_ID)
    # notion.some_method()

if __name__ == "__main__":
    main()
