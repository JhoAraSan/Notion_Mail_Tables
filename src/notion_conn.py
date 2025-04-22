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
        print(f"✅ Página creada correctamente: {response.status_code}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Error creando la página: {e}")
        return False