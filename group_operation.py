from load_functions import salva_os_grupos

def criar_grupo(users, user_login, groups):
    """
    Cria um grupo
    O usuário 0 é o administrador
    """
    while True:
        new_group_name = input("\nNome do grupo: ")
        if new_group_name in groups:
            print("Ja existe um grupo com esse nome.")
        else:
            user = users[user_login]
            groups[new_group_name] = [user['nickname']]
            salva_os_grupos(groups)
            print(f"\nGrupo criado com sucesso {user['nickname']}.")
            break





