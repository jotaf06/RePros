from singning_up import find_user

def show_perfil(users):
    """Mostra as informações associadas a um perfil com base no nickname fornecido"""
    while True:
        perfil_nickname = input("\nForneça o nickname do perfil: ")
        user = find_user(users, perfil_nickname)

        if user is None:
            print("\nNão há usuário com esse perfil.")
        else:
            print("\n")
            for key, value in user.items():
                if key != 'password':
                    print(f"{key}: {value}")

        continuar = input("\nDigite 'True' para continuar ou 'False' para parar a operação: ")
        if continuar.lower() != 'true':
            break