import json

users = []
groups = []

def load_users():
    """Carrega os usuários existentes na rede"""
    try:
        file_name = 'users_info.json'
        with open(file_name, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []
        
 
def verifying_repeatted_user_info(info_type, new_info):
    """Verifica se dada informação pertence a um usuário"""
    if len(users) == 0:
        return True
    else:
        for user in users:
            if user[info_type] == new_info:
                return False
        return True
    
def new_login_user():
    """Determina um novo login válido"""
    user_login = input('Digite seu novo login: ')
    while True:
        if verifying_repeatted_user_info('login', user_login):
            print('Login válido!!')
            break
        else:
            print('Esse login ja existe')
            user_login = input('Digite um outro login: ')
    return user_login

def new_nickname_user():
    """Determina um noco nickname válido"""
    user_nickname = input('Digite seu nickname: ')
    while True:
        if verifying_repeatted_user_info('nickname', user_nickname):
            print('nickname válido!!')
            break
        else:
            print('Esse nickname ja existe')
            user_nickname = input('Digite um outro nickname')

    return user_nickname

def create_new_user():
    """Cria um novo usuário"""
    user_age = int(input('Infome a sua idade: '))
    if user_age < 18:
        print('Você não tem idade suficiente para usar a rede.')
        return None 

    user_login = new_login_user()
    user_nickname = new_nickname_user()

    user_password = input('Digite sua senha: ')

    new_user = ({
        'login' : user_login,
        'password' : user_password,
        'nickname' : user_nickname,
        'privacity': 1})
    
    users.append(new_user)
    return new_user

def edit_user(user):
    """Edita as informações do usuário"""

    print("Vamos editar as informações de seu perfil\n")
    print("Você tem as seguinte ações possíveis:")
    print("0. Digite a Para mostrar na tela as opções 1,2,3,4.")
    print("1. Digite l para mudar seu login.")
    print("2. Digite n para mudar seu nickname.")
    print("3. Digite s para mudar a sua senha.")
    print("4. Digite q para sair do modo de edição de informações")

    while True:
        info_to_change = input("Qual informação você gostaria de mudar?")

        if info_to_change == 'a':
            print("Você tem as seguinte ações possíveis:")
            print("0. Digite a Para mostrar na tela as opções 1,2,3,4.")
            print("1. Digite l para mudar seu login.")
            print("2. Digite n para mudar seu nickname.")
            print("3. Digite s para mudar a sua senha.")
            print("4. Digite q para sair do modo de edição de informações")

        elif info_to_change == "l":
            user['login'] = new_login_user()
            
        elif info_to_change == "n":
            user['nickname'] = new_nickname_user()
        
        elif info_to_change == "s":
            user['password'] = input("Digite sua nova senha: ")
            print("Senha alterada com sucesso!!")
        
        elif info_to_change == "q":
            print(user, 'Seu usuário foi editado!!')
            break
    
    

def delete_user(user):
    for x in users:
        if x == user:
            users.remove(x)
            
def privacity(user):
    for x in users:
            if x['privacity'] == user['privacity']:
                x['privacity'] = 0

def add_member(new_member, group):
    group.append(new_member)

def find_user(user_login):
    for user in users:
        if user['login'] == user_login:
            return user
    return None

users = load_users()

print("Bem vindo a rede RePros!")
print("Você tem as seguintes opções nessa rede:\n")

print("Digite 'criar' para criar uma conta")
print("Digite 'editar' para editar as informações da sua conta")
print("Digite d para deletar, permanentemente, sua conta")
print("Digite a para acessar as informações de um usuário")
print("Digite ad para adicionar um novo membro em um grupo")
print("Digite s para se desligar da rede\n")
print("Digite opt para ver essas opções anteriores novamente.")

while True:
    action = input("O que você deseja fazer?: ").lower()

    if action == 'criar':
        new_user = create_new_user()
        print(new_user)

    elif action == 'editar':
        user_login = input("Informe seu login: ")
        user = find_user(user_login)

        if user == None:
            print("\nEsse login não está cadastrado na rede.")
            print("Operação inválida!!")
            print("Saindo do modo de edição\n")
        else:
            edit_user(user)

    elif action == 'p':
        privacity(users[0])
        print(users, 'O acesso ao perfil do seu usuário foi restringido!!')

    elif action == 'a':
        # vamos criar um grupo exemplo pra mostrar a funcionalidade
        # da add_member
        # Também vamos considerar que temos dois membros iniciais
        create_new_user()
        create_new_user()

        group = []
        group.append(users[0])
        group.append(users[1])

        # vamos criar um usuário e colocá-lo
        create_new_user()
        add_member(users[2], group)

        print(groups, 'Seu novo membro foi adicionado!!')

    elif action == 'r':
        # vamos adicionar um usuário e depois removê-lo
        create_new_user()
        delete_user(users[0])

        print(users, 'Seu usuário foir removido!!')

    elif action == 's':
        file_name = 'users_info.json'
        with open(file_name, 'w') as f:
            json.dump(users, f)
        break

    elif action == "opt":
        print("Digite c para criar uma conta")
        print("Digite e para editar as informações da sua conta")
        print("Digite d para deletar, permanentemente, sua conta")
        print("Digite a para acessar as informações de um usuário")
        print("Digite ad para adicionar um novo membro em um grupo")
        print("Digite s para se desligar da rede\n")


    
