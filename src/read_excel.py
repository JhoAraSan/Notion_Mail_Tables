# modules/read_excel.py
import pandas as pd #pip install pandas openpyxl
import datetime
import win32com.client #pip install pywin32

def read_excel_file(file_path, sheet_name,header,usecols,skiprows,nrows):
    """
    Lee un archivo Excel y devuelve los datos de una hoja específica como una lista de diccionarios.
    
    Args:
        file_path (str): Ruta del archivo Excel.
        sheet_name (str): Nombre de la hoja a leer.

    Returns:
        list[dict]: Lista de filas como diccionarios (columnas como claves).
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name,header=header,usecols=usecols,skiprows=skiprows,nrows=nrows) # Cambia el rango de filas según sea necesario
        records = df.to_dict(orient="records")
        msn=f"✅ Hoja '{sheet_name}' leída. # Filas: {len(records)}"
        return records, msn
    except Exception as e:
        msn=f"❌ Error leyendo el Excel: {e}"
        return [], msn
    
def data(Nombre,fecha):
    if isinstance(fecha,(datetime.date, datetime.datetime,pd.Timestamp)): #aqui reconoce tres tipos de fecha
        fecha_fin = fecha.strftime("%Y-%m-%d") # Cambia el formato según sea necesario
        dias = datetime.date.today() - fecha.date()
    else:
        fecha_fin = str(fecha)
    # Aquí puedes definir las propiedades que deseas enviar a Notion
    properties = {
        "Nombre": {
            "title": [
                {
                    "text": {
                        "content": str(Nombre)
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
    return properties