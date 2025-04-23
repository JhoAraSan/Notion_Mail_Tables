from dotenv import load_dotenv
import os
import sys
from read_excel import read_excel_file
from notion_conn import *
from mensaje import mostrar_mensaje_final
import pandas as pd
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
        fecha = fila[6] # Cambia el índice según la columna que necesites
        if isinstance(fecha,(datetime.date, datetime.datetime,pd.Timestamp)): #aqui reconoce tres tipos de fecha
            fecha_fin = fecha.strftime("%Y-%m-%d") # Cambia el formato según sea necesario
            dias = datetime.date.today() - fecha.date()
        else:
            fecha_fin = str(fecha)
            print(f'Pase por aca wajaja {fecha_fin} vs {fecha}') # Cambia el formato según sea necesario
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
            },
            "Dias": {
                "number": int(dias.days) 
            }
        }
        
        page_id = get_notion_database( NOTION_TOKEN,NOTION_DATABASE_ID, fila[5])

        if page_id:
            update_notion_page( NOTION_TOKEN, page_id, properties)
        else:
            create_notion_page(NOTION_DATABASE_ID, NOTION_TOKEN, properties)
    
    mostrar_mensaje_final()

if __name__ == "__main__":
    main()
