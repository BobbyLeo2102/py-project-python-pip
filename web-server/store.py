import requests

def get_categories():
    try:
        r = requests.get('https://api.escuelajs.co/api/v1/categories')
        r.raise_for_status()  # Verificar si hay errores de solicitud HTTP
        print(r.status_code)
        print(r.text)
        print(type(r.text))
        categories = r.json()#Con el metodo json podemos transformar los elementos en una lista que python puede reconocer e iterar con sus elementos
        for category in categories:
            print(category['name'])
    except Exception as e:
        print('Error:', e)

get_categories()
