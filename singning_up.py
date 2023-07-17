from load_functions import salva_os_usuarios

def find_user(users, perfil_nickname):
    """Procura o usuário que possui tal nickname"""
    for user in users.values():
        if user['nickname'] == perfil_nickname:
            return user
    return None

def new_login_user(users):
    """Determina um novo login válido"""
    new_user_login = input('\nDigite seu novo login: ')
    while True:
        if new_user_login not in users:
            print('Login válido!!')
            return new_user_login
        else:
            print('Esse login ja existe')
            new_user_login = input('\nDigite um outro login: ')

def new_nickname_user(users):
    """Determina um novo nickname válido"""
    new_user_nickname = input('\nDigite seu novo nickname: ')
    while True:
        if find_user(users, new_user_nickname) == None:
            print('\nnickname válido!!')
            return new_user_nickname
        else:
            print('\nEsse nickname ja existe')
            new_user_nickname = input('\nDigite um outro nickname: ')

def create_new_user(users):
    """Cria um novo usuário"""

    user_login = new_login_user(users)
    user_nickname = new_nickname_user(users)
    user_password = input('\nDigite sua senha: ')

    new_user = {'password' : user_password,
                'nickname' : user_nickname,
                'privacity' : 0}
    
    users[user_login] = new_user
    
    salva_os_usuarios(users)
    
