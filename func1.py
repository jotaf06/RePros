import json

users = {}
groups = []

def load_users():
    """Carrega os usuários existentes na rede"""
    try:
        file_name = 'users_info.json'
        with open(file_name, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}
        
     
def new_login_user():
    """Determina um novo login válido"""
    new_user_login = input('Digite seu novo login: ')
    while True:
        if not(new_user_login in users):
            print('Login válido!!')
            break
        else:
            print('Esse login ja existe')
            new_user_login = input('Digite um outro login: ')
    return new_user_login

def new_nickname_user():
    """Determina um novo nickname válido"""
    new_user_nickname = input('Digite seu nickname: ')
    while True:
        if not(new_user_nickname in users):
            print('nickname válido!!')
            return new_user_nickname
        else:
            print('Esse nickname ja existe')
            new_user_nickname = input('Digite um outro nickname')


def create_new_user():
    """Cria um novo usuário"""
    user_age = int(input('Infome a sua idade: '))
    if user_age < 18:
        print('Você não tem idade suficiente para usar a rede.')
        return None

    user_login = new_login_user()
    user_nickname = new_nickname_user()

    user_password = input('Digite sua senha: ')

    new_user = {'password' : user_password,
                'nickname' : user_nickname,
                'privacity' : 0}
    
    users[user_login] = new_user
    return new_user

def edit_user(user_login):
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
            new_login = new_login_user()
            users[new_login] = users[user_login]
            del users[user_login]
            user_login = new_login
            
        elif info_to_change == "n":
            user = users[user_login] 
            user['nickname'] = new_nickname_user()
        
        elif info_to_change == "s":
            user = users[user_login]
            user['password'] = input("Digite sua nova senha: ")
            print("Senha alterada com sucesso!!")
        
        elif info_to_change == "q":
            print(users[user_login], 'Seu usuário foi editado!!')
            break
    

def delete_user(user):
    for x in users:
        if x == user:
            users.remove(x)
            
def privacity():
    """Torna o acesso as informações do usuário restrito"""
    print("\nPor favor digite seu login para") 
    print("que possamos tornar seu perfil restrito\n")

    user_login = input("Digite seu login: ")

    while True:
        user = find_user(user_login)
        if user:
            user['privacity'] = 1
            print("Suas informações agora são restritas.")
            print("Veja: ", user['privacity'])
            break
        else:
            print("Login não encontrado!!")
            user_login = input("Digite o login novamente ou digite 'sair' para desistir da operação: ")
            if user_login == "sair":
                break
    
    print("Saindo do modo de privatização.\n")

def add_member(new_member, group):
    group.append(new_member)

def find_user(user_login):
    """Encontra um usuário a partir de seu login"""
    if user_login in users:
        True
    return False

"""
def create_new_group():
    print("Vamos criar um novo grupo.")
    print("Por favor digite seu login para que possamos criar o grupo")
    print("e lhe fornecer permissão de administrador.\n")

    user_login = input("Informe seu login: ")
    
    user = find_user(user_login)
    if user:

        file_name = 'repros_groups.json'
        with open(file_name) as f:
"""    

users = load_users()

print("Bem vindo a rede RePros!")
print("Você tem as seguintes opções nessa rede:\n")

print("Digite 'criar_usuario' para criar uma conta")
print("Digite 'editar_usuario' para editar as informações da sua conta")
print("Digite 'privado' para tornar um perfil restrito")
print("Digite 'criar_grupo' para criar um novo grupo")
print("Digite d para deletar, permanentemente, sua conta")
print("Digite a para acessar as informações de um usuário")
print("Digite ad para adicionar um novo membro em um grupo")
print("Digite s para se desligar da rede\n")
print("Digite opt para ver essas opções anteriores novamente.")

while True:
    action = input("\nO que você deseja fazer?: ").lower()

    if action == "criar_usuario":
        new_user = create_new_user()
        
        if new_user:
            print(new_user)

    elif action == "editar_usuario":
        user_login = input("Informe seu login: ")

        if user_login in users:
            edit_user(user_login)
        else:
            print("\nEsse login não está cadastrado na rede.")
            print("Operação inválida!!")
    
        print("Saindo do modo de edição\n")

    elif action == "privado":
        privacity()
        print("Encerrando modo de operação.")

    elif action == 'criar_grupo':
       
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
            json.dump(users, f, indent='\t')
        break

    elif action == "opt":
        print("Digite c para criar uma conta")
        print("Digite e para editar as informações da sua conta")
        print("Digite d para deletar, permanentemente, sua conta")
        print("Digite a para acessar as informações de um usuário")
        print("Digite ad para adicionar um novo membro em um grupo")
        print("Digite s para se desligar da rede\n")


    
print(users)