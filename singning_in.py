from editar_usuario import edit_user
from acesso_a_perfil import show_perfil

def entrando_na_rede_repros(users, user):
    """Aqui ocorre toda a interação do usuário com a rede"""
    
    print(f"Olá {users[user]['nickname']} Você está conectado a rede.")
     
    sair_da_rede = False
    while sair_da_rede == False:
        print("Digite 'lista_de_comandos', para ver os comandos da rede.\n")
        command = input("comando : ")

        if command == "lista_de_comandos":
            print("\n'editar_usuario' - edita as informações associadas a um usuário.")
            print("'acessar_perfil' - para acessar as informações/arquivos de um usuário.")
            print("'mensagem' - enviar uma mensagem a outro usuario.")
            print("'criar_grupo' - cria um grupo.")
            print("'adicionar_midia' - adiciona arquivos em seu perfil.")  
            print("'sair' - para se desconectar.\n")  
        
        elif command == 'acessar_perfil':
            show_perfil(users)

        elif command == 'sair':
            sair_da_rede = True
            print("Desconectando...\n")
        
        elif command == 'editar_usuario':
            edit_user(user)

