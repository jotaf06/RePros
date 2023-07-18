from editar_usuario import edit_user
from acesso_a_perfil import show_perfil
from group_operation import criar_grupo, entrar_grupo
from add_amigo import adiciona_amigo    
from upload import upload_arquivo

def entrando_na_rede_repros(users, user_login, groups, relations):
    """Aqui ocorre toda a interação do usuário com a rede"""
    
    print(f"Olá {users[user_login]['nickname']} Você está conectado a rede.")
     
    sair_da_rede = False
    while sair_da_rede == False:
        print("Digite 'lista_de_comandos', para ver os comandos da rede.\n")
        command = input("comando : ")

        if command == "lista_de_comandos":
            print("\n'editar_usuario' - edita as informações associadas a um usuário.")
            print("'acessar_perfil' - para acessar as informações/arquivos de um usuário.")
            print("'add_amido' - adiciona um amigo.")
            print("'subir_arquivo' - subir conteúdo no perfil.")
            print("'criar_grupo' - cria um grupo.")
            print("'entrar_grupo' - entrar em um grupo.")
            print("'adicionar_midia' - adiciona arquivos em seu perfil.")  
            print("'sair' - para se desconectar.\n")  
        
        elif command == 'editar_usuario':
            edit_user(users, user_login)

        elif command == 'acessar_perfil':
            show_perfil(users)

        elif command == 'add_amigo':
            adiciona_amigo(user_login, relations)

        elif command == 'subir_arquivo':
            upload_arquivo(users[user_login]['nickname'])
            
        elif command == 'criar_grupo':
            criar_grupo(users, user_login, groups)

        elif command == 'entrar_grupo':
            entrar_grupo(users, user_login, groups)

        elif command == 'sair':
            sair_da_rede = True
            print("Desconectando...\n")
        
        

