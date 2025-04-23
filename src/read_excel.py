# modules/read_excel.py
import pandas as pd #pip install pandas openpyxl

def read_excel_file(file_path, sheet_name):
    """
    Lee un archivo Excel y devuelve los datos de una hoja específica como una lista de diccionarios.
    
    Args:
        file_path (str): Ruta del archivo Excel.
        sheet_name (str): Nombre de la hoja a leer.

    Returns:
        list[dict]: Lista de filas como diccionarios (columnas como claves).
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name,header=None,usecols="F:G",skiprows=4,nrows=19) # Cambia el rango de filas según sea necesario
        records = df.to_dict(orient="records")
        msn=f"✅ Hoja '{sheet_name}' leída. # Filas: {len(records)}"
        return records, msn
    except Exception as e:
        msn=f"❌ Error leyendo el Excel: {e}"
        return [], msn