import requests #pip install requests

def create_notion_page(token, database_id, properties):
    """
    Crea una nueva página en un database de Notion.

    :param token: Token de la integración de Notion.
    :param database_id: ID del database de Notion.
    :param properties: Propiedades a escribir en la nueva página.
    :return: True si fue exitoso, False si hubo error.
    """
    url = "https://api.notion.com/v1/pages"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    payload = {
        "parent": {"database_id": database_id},
        "properties": properties
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        msn=f"✅ Página creada correctamente: {response.status_code}"
        return True, msn
    except requests.exceptions.RequestException as e:
        msn=f"❌ Error creando la página: {e}"
        return False, msn
    
def get_notion_database(token, database_id,nombre):
    """
    Obtiene el contenido de un database de Notion.

    :param token: Token de la integración de Notion.
    :param database_id: ID del database de Notion.
    :return: Contenido del database.
    """
    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "filter": {
            "property": "Nombre",
            "rich_text": {
                "equals": nombre
            }
        }
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        if response.status_code == 200 and not response.json().get("results"):
            msn=f"❌ No se encontró el database con el nombre: {nombre}"
            return None,msn
        else:
            return response.json().get("results", [])[0]["id"], "✅ Id encontrado correctamente"
    except requests.exceptions.RequestException as e:
        msn=f"❌ Error obteniendo el database: {e}"
        return None,msn

def update_notion_page(token, page_id, properties):
    """
    Actualiza una página en un database de Notion.

    :param token: Token de la integración de Notion.
    :param page_id: ID de la página a actualizar.
    :param properties: Propiedades a actualizar en la página.
    :return: True si fue exitoso, False si hubo error.
    """
    url = f"https://api.notion.com/v1/pages/{page_id}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    payload = {
        "properties": properties
    }

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        msn=f"✅ Página actualizada correctamente: {response.status_code}"
        return True, msn
    except requests.exceptions.RequestException as e:
        msn=f"❌ Error actualizando la página: {e}"
        return False, msn

def G_U_C_data(msns:list, Nombre, NOTION_TOKEN, NOTION_DATABASE_ID, properties):
    page_id, msn = get_notion_database( NOTION_TOKEN,NOTION_DATABASE_ID, Nombre)
    msns.append(msn)

    if page_id==None:
        msns.append(create_notion_page( NOTION_TOKEN,NOTION_DATABASE_ID, properties)[1])
    else:
        msns.append(update_notion_page( NOTION_TOKEN, page_id, properties)[1])
    return msns