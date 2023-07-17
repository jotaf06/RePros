from singning_up import create_new_user
from singning_in import entrando_na_rede_repros
from load_functions import carrega_usuarios, carrega_os_grupos

users = carrega_usuarios()
groups = carrega_os_grupos()

print("BEM VINDO A REDE RePros!\n")
print("ATENÇÃO: Os comandos da rede devem ser fornecidos exatamente como forem apresentados.")

exit = False
while not exit:

    print("\n'sing_in' - entrar na rede, caso ja possua um usuário.")
    print("'sing_up' - cadastra um usuário.")
    print("'exit' - Desliga a aplicação.\n")
    command = input("Digite um comando: \n")

    if command == 'sing_in':
        input_login = input("login: ")
        input_password = input("senha: ")

        if input_login not in users:
            print("Usuário inexistente. Esse login não está cadastrado na rede.")
            print("Abordando operação sing_in...\n")
        else:
            if users[input_login]['password'] != input_password:
                print("Senha inválida!!!\n")
            else:            
                print("sing_in realizado com sucesso, entrando na rede RePros...\n")
                entrando_na_rede_repros(users, input_login, groups)
    
    elif command == 'sing_up':
        print("Você tem mais de 18 anos? Digite sua respota no seguinte formato:\n")
        print("'sim' - caso tenha idade maior ou igual a 18 anos.")
        print("'nao' - caso seja menor de idade.\n")
        age = input("Resposta: ")

        if age == 'sim':
            create_new_user(users)
        
        elif age == 'nao':
            print("Você não tem idade suficiente para ser um usuário dessa rede.\n\n")
    
    elif command == 'exit':
        exit = True
