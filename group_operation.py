from load_functions import salva_os_grupos

def criar_grupo(users, user_login, groups):
    """Cria um grupo. O usuário 0 é o administrador"""
    while True:
        new_group_name = input("\nNome do grupo: ")
        if new_group_name in groups:
            print("Ja existe um grupo com esse nome.")
        else:
            user = users[user_login]
            groups[new_group_name] = [[user['nickname'], 'admin']]
            salva_os_grupos(groups)
            print(f"\nGrupo criado com sucesso {user['nickname']}.")
            break

def add_membro(user_membro, groups, group):
    """Adiciona um membro"""
    if not (user_membro[1] == 'admin' or user_membro[1] == 'sub_admin'):
        print("Você não tem permissão para realizar essa operação...")

    elif user_membro[1] == 'admin':
        print("\nOlá admin")
        new_membro_nickname = input("Quem você deseja adicionar no seu grupo?: ")
        cargo = input("Qual o nível de acesso do usuário?: ")

        group.append([new_membro_nickname, cargo])
        salva_os_grupos(groups)
        print("Operação bem sucedida.")

def eh_membro(user_nickname, group):
    """Verifica se um usuario eh membro de certo grupo"""
    for user in group:
        if user[0] == user_nickname:
            return user
    return None

def entrar_grupo(users, user_login, groups):
    """Aqui acontece a interação do usuario com o grupo"""
    group_name = input("\nGrupo que se deseja entrar: ")

    if group_name not in groups:
        print("Esse grupo não existe.")
    else:
        group = groups[group_name]
        user_nickname = users[user_login]['nickname']
        print(user_nickname)
        user_membro = eh_membro(user_nickname, group)
        if user_membro != None:
            print(f"\nBem vindo a {group_name}, {user_nickname}.")
            
            while True:
                print("\n'add_membro' - para adicionar membro.")
                print("'sair' - para sair do grupo.\n")
                
                command = input("comando: ")
                if command == 'add_membro':
                    add_membro(user_membro, groups, group)

                elif command == 'sair':
                    print("Saindo do grupo...")
                    break
        
        else:
            print("Você não é membro desse grupo!")



