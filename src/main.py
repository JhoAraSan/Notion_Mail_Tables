from dotenv import load_dotenv
import os
import sys
from read_excel import *
from notion_conn import *
from mensaje import mostrar_mensaje_final

def vars_env():
    ENV_PATH = "list.env"
    try:
        with open(ENV_PATH, 'r') as f:
            pass  # Solo para verificar que el archivo existe
    except FileNotFoundError:
        msn=f"❌ Error: el archivo {ENV_PATH} no se encontró."
        sys.exit(1)

    load_dotenv(dotenv_path="list.env")

    try:
        NOTION_TOKEN = os.getenv("NOTION_TK")
        NOTION_DATABASE_ID = os.getenv("NOTION_DB")
        NOTION_DATABASE_ID_2 = os.getenv("NOTION_DB_2")
        EXCEL_FILE_PATH = os.getenv("EXC_PATH")
        EXCEL_SHEET_NAME = os.getenv("EXC_PG")
        EXCEL_SHEET_COLS = os.getenv("EXC_PG_COLS")
        EXCEL_SHEET_NAME_2 = os.getenv("EXC_PG_2")
        EXCEL_SHEET_COLS_2 = os.getenv("EXC_PG_2_COLS")
    except KeyError as e:
        msn=f"❌ Error: la variable de entorno {e} no está definida."
        sys.exit(1)

    msn="✅ Variables cargadas correctamente."
    return NOTION_TOKEN, NOTION_DATABASE_ID, NOTION_DATABASE_ID_2, EXCEL_FILE_PATH, EXCEL_SHEET_NAME,EXCEL_SHEET_COLS, EXCEL_SHEET_NAME_2,EXCEL_SHEET_COLS_2, msn

def main():
    msns=[]
    NOTION_TOKEN, NOTION_DATABASE_ID, NOTION_DATABASE_ID_2, EXCEL_FILE_PATH, EXCEL_SHEET_NAME,EXCEL_SHEET_COLS,EXCEL_SHEET_NAME_2,EXCEL_SHEET_COLS_2,msn= vars_env()
    msns.append(msn)

    # Leer el archivo Excel Servicios
    datos_excel,msn = read_excel_file(EXCEL_FILE_PATH, EXCEL_SHEET_NAME,header=None,usecols=EXCEL_SHEET_COLS,skiprows=4,nrows=19)
    msns.append(msn)
    if datos_excel is None:
        msns.append("❌ Error: no se pudieron leer los datos del archivo Excel.")
        sys.exit(1)
    for fila in datos_excel:
        properties=data(fila[5],fila[6])
        G_U_C_data(msns, fila[5], NOTION_TOKEN, NOTION_DATABASE_ID, properties)
    
    # Leer el archivo Excel Apps
    datos_excel,msn = read_excel_file(EXCEL_FILE_PATH, EXCEL_SHEET_NAME_2,header=None,usecols=EXCEL_SHEET_COLS_2,skiprows=21,nrows=12)
    msns.append(msn)
    if datos_excel is None:
        msns.append("❌ Error: no se pudieron leer los datos del archivo Excel.")
        sys.exit(1)
    for fila in datos_excel:
        properties=data(fila[7],fila[8])
        G_U_C_data(msns, fila[7], NOTION_TOKEN, NOTION_DATABASE_ID_2, properties)
    
    mostrar_mensaje_final(msns)

if __name__ == "__main__":
    main()
