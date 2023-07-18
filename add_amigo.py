from load_functions import salva_amizades

def adiciona_amigo(user_login, relations):
    new_friend_nickname = input("\nQual seu novo amigo?: ")
    
    if user_login not in relations:
        relations[user_login] = [new_friend_nickname]
    else:
        relations[user_login].append(new_friend_nickname)
    
    salva_amizades(relations)

    print("Amigo adicionado!!\n")
    
