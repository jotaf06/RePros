from load_users import carrega_usuarios, salva_os_usuarios

users = carrega_usuarios() 

def new_login_user():
    """Determina um novo login válido"""
    new_user_login = input('\nDigite seu novo login: ')
    while True:
        if new_user_login not in users:
            print('Login válido!!\n')
            return new_user_login
        else:
            print('Esse login ja existe')
            new_user_login = input('Digite um outro login: ')

def new_nickname_user():
    """Determina um novo nickname válido"""
    new_user_nickname = input('\nDigite seu novo nickname: ')
    while True:
        if new_user_nickname not in users:
            print('nickname válido!!\n')
            return new_user_nickname
        else:
            print('Esse nickname ja existe')
            new_user_nickname = input('Digite um outro nickname')

def create_new_user():
    """Cria um novo usuário"""

    user_login = new_login_user()
    user_nickname = new_nickname_user()
    user_password = input('\nDigite sua senha: ')

    new_user = {'password' : user_password,
                'nickname' : user_nickname,
                'privacity' : 0}
    
    users[user_login] = new_user
    
    salva_os_usuarios(users)
    
