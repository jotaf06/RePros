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

def carrega_os_grupos():
    """Carrega os grupos"""
    try:
        file_name = 'groups.json'
        with open(file_name, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}
    
def salva_os_grupos(groups):
    """Salva os grupos em arquivo JSON"""
    with open('groups.json', 'w') as file:
        json.dump(groups, file, indent='\t')

def carrega_amizades():
    """Carrega as amizades"""
    try:
        with open('amigos.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

def salva_amizades(relationship):
    """Salva as amizades"""
    with open('amigos.json', 'w') as file:
        json.dump(relationship, file, indent='\t')