# 📊 Sincronizador Automático de Excel a Notion

Este proyecto permite **leer datos de un archivo Excel** específico, procesarlos (incluso manejando fechas) y **actualizarlos automáticamente en una base de datos de Notion**.  
Además, está diseñado para **ejecutarse de forma automática** al iniciar el sistema operativo Windows, mostrando una pequeña notificación al finalizar.

---

## 🚀 Funcionalidades principales

- Lectura de un rango específico dentro de una hoja de Excel.
- Procesamiento de fechas y cálculo de días.
- Creación o actualización de registros en una base de datos de Notion.
- Registro de mensajes de estado en pantalla (sin repeticiones).
- Ejecución automática al inicio del sistema operativo.

---

## 🛠️ Requisitos

- Python 3.10 o superior
- Librerías:
  - `pandas`
  - `openpyxl`
  - `requests`
  - `python-dotenv`

(Instalables fácilmente con `pip install -r requirements.txt`)

---

## ⚙️ Variables de entorno (.env)

Debes crear un archivo llamado `.env` en la raíz del proyecto con el siguiente contenido:

```dotenv
NOTION_TOKEN=ntn_tu_token_aqui
NOTION_DATABASE_ID=tu_database_id_aqui
EXCEL_FILE_PATH=ruta\completa\a\tu\archivo.xlsx
EXCEL_SHEET_NAME=nombre_de_la_hoja
```

### Explicación:

NOTION_TOKEN: Tu "Internal Integration Secret" de Notion (empieza por ntn_).
NOTION_DATABASE_ID: ID de la base de datos en Notion donde se crearán o actualizarán los registros.
EXCEL_FILE_PATH: Ruta absoluta de tu archivo de Excel.
EXCEL_SHEET_NAME: Nombre de la hoja dentro del Excel que contiene los datos.

---

## 🔥 Configurar ejecución automática en Windows

1. Crea un archivo .bat que ejecute tu script de Python, por ejemplo:

```bash
Copy
Edit
@echo off
cd  x:/ruta_de_tu_proyecto
python x:/ruta_de_tu_proyecto/scr/main.py
exit
```
> Si usaste un entorno virtual, cambia `python` por la ruta del ejecutable de tu entorno virtual, algo como `x:/path/.conda/envs/notion/python.exe`

2. Presiona Win + R → escribe shell:startup → Enter.

3. Copia y pega tu archivo .bat en esa carpeta.

¡Listo! El script se ejecutará automáticamente cada vez que inicies Windows.

---

## 📌 Notas adicionales

- Asegúrate de no dejar el archivo de Excel abierto durante la ejecución.
- Maneja con cuidado el archivo .env para no exponer tus credenciales.
- Puedes agregar logs de ejecución si quieres llevar un control más detallado.

---
---

## 🔐 Seguridad y Encriptación de Credenciales (BONUS)

Este proyecto implementa un sistema de cifrado para proteger las contraseñas sensibles almacenadas en el archivo `.env`.

Se incluye el archivo `encode.py` para facilitar la **generación de claves** y la **encriptación de valores sensibles**, como tu token de Notion.

### 📌 ¿Cómo funciona?

El sistema utiliza la librería `cryptography` y está basado en `Fernet`, un método de cifrado simétrico de alto nivel.

### 1️⃣ Generar la clave secreta

Este paso **solo se realiza una vez**. Crea un archivo `secret.key` que se usará para cifrar y descifrar.

```bash
python encode.py
```

Cuando te pregunte por una contraseña, presiona Enter sin escribir nada. Verás el mensaje:

```vbnet
Gen Key
🔑 Clave generada y guardada en 'secret.key'
```

⚠️ Guarda secret.key con mucho cuidado y no lo subas nunca a GitHub.

### 2️⃣ Encriptar un valor

Cada vez que necesites cifrar una nueva contraseña o token:

```bash
python encode.py
```

Esta vez, escribe el valor que deseas cifrar (ej. tu Notion Token). Se imprimirá algo como:

```css
Contraseña encriptada:
gAAAAABk..
```

Copia ese texto y pégalo en tu archivo .env como valor, por ejemplo:

```dotenv
NOTION_TOKEN_ENCRYPTED=gAAAAABk...
```

### 3️⃣ Desencriptar en tu script principal

Tu script de Python principal usará cryptography para leer secret.key, descifrar el valor, y usarlo de forma segura.
Asegúrate de tener una función para eso, por ejemplo:

### ✅ Recomendaciones de seguridad

- Nunca subas `.env` ni `secret.key` a GitHub. Usa `.gitignore`. para no incluirlas  
- Usa contraseñas fuertes y actualízalas periódicamente.


