import json

def carrega_usuarios():
    """Carrega os usuários existentes na rede"""
    try:
        file_name = 'users.json'
        with open(file_name, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

def salva_os_usuarios(users):
    """Salva os usuários em um arquivo JSON"""
    with open('users.json', 'w') as file:
        json.dump(users, file, indent='\t')