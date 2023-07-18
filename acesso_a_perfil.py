import os
from singning_up import find_user

def show_perfil(users):
    """Mostra as informações associadas a um perfil com base no nickname fornecido"""
    while True:
        perfil_nickname = input("\nForneça o nickname do perfil: ")
        user = find_user(users, perfil_nickname)

        if user is None:
            print("\nNão há usuário com esse perfil.")
        else:
            perfil_dir = os.path.join('RePros', user['nickname'])
            files = os.listdir(perfil_dir)
            if len(files) == 0:
                print("Não há arquivos no perfil.")
            else:
                print("Arquivos no perfil:")
                for file in files:
                    print(file)

        continuar = input("\nDigite 'True' para continuar ou 'False' para parar a operação: ")
        if continuar.lower() != 'true':
            break
