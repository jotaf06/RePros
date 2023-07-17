from load_functions import salva_os_usuarios
from singning_up import new_login_user, new_nickname_user

def privacity_edit(users, user_login):
    """Torna o acesso as informações do usuário restrito"""
    user = users[user_login]
    if user['privacity'] == 0:
        print("\nSeu usuário tem o perfil aberto.")

    elif user['privacity'] == 1:
        print("\nSeu usuário tem o perfil fechado.")

    print("'privado' - mantem ou torna privado.")
    print("'aberto' - mantem ou torna aberto.\n")

    command = input("comando_de_privacidade: ")

    if command == 'privado':
        user['privacity'] = 0
    elif command == 'aberto':
        user['privacity'] = 1

def remove_user(users, user_login):
    """Deleta um usuario da rede"""
    print("\nTem certeza que deseja deletar seu usuario?\n")
    print("'del' - para deletar")
    print("'cancelar' - cancelar delecao de usuario,\n")

    command = input("commando_de_delecao: ")
    if command == 'del':
        del users[user_login]
        return True
    
    elif command == 'cancelar':
        print("Operação abordada...\n")
        return False
        

def edit_user(users, user_login):
    """Edita as informações do usuário"""
    
    print("\n'opts' - mostra as opções de edição.")
    print("'login' - altera seu login.")
    print("'nickname' - altera o nickname")
    print("'senha' - muda a senha")
    print("'editar_privacidade' bloqueia/desbloqueia o acesso as suas informações.")
    print("'delecao_de_conta' - apaga o usuario e todo conteúdo associado a ele da rede.")
    print("'sair' - sair do modo de edição.\n")

    while True:
        command = input("commando de edição: ")

        if command == 'opts':
            print("\n'opts' - mostra as opções de edição.")
            print("'login' - altera seu login.")
            print("'nickname' - altera o nickname")
            print("'senha' - muda a senha")
            print("'editar_privacidade' bloqueia/desbloqueia o acesso as suas informações.")
            print("'delecao_de_conta' - apaga o usuario e todo conteúdo associado a ele da rede.")
            print("'sair' - sair do modo de edição.\n")

        elif command == 'login':
            new_login = new_login_user(users)

            users[new_login] = users[user_login]
            del users[user_login]
            user_login = new_login
            
        elif command == 'nickname':
            user = users[user_login] 
            user['nickname'] = new_nickname_user(users)
        
        elif command == 'senha':
            user = users[user_login]
            user['password'] = input("Digite sua nova senha: ")
            print("Senha alterada com sucesso!!\n")
        
        elif command == 'editar_privacidade':
            privacity_edit(users, user_login)

        elif command == 'delecao_de_conta':
            remocao = False
            remocao = remove_user(users, user_login)
            
            if remocao:
                print("Usuario removido, saindo da aplicação.")
                exit()

        elif command == 'sair':
            salva_os_usuarios(users)
            print(users[user_login], "Encerrando operação de edição...\n")
            break