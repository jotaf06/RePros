usersList = []
groupsList = []

def new_user():

    idade = int(input('Infome a sua idade: '))
    if idade < 18:
        print('Você não tem idade suficiente para usar a rede.')
        return None 

    userLogin = input('Insert your Login: ')
    userName = input('Insert your nickname: ')  
    userPassword = input('What password would you like to use for this account? ')

    confirmPassword = input('Confirm your password: ')
    while confirmPassword != userPassword:
        print('Confirm failed ')
        print('Try again ')
        confirmPassword = input('Confirm your password: ')

    usersList.append({'login' : userLogin, 'password' : userPassword, 'nickname' : userName, 'privacity': 1})
    print('Your account was created! ')

def edit_user(currentUser):
    print("Let's change your info")
    print('1. press "u" to change user.')
    print('2. press "p" to change password.')
    action = input('What info would you like to change?')

    new_info = ''
    if action == 'u':
        new_info = input('Type your new nick:')
        for x in usersList:
            if x['nickname'] == currentUser['nickname']:
                x['nickname'] = new_info

    elif action == 'p':
        new_info = input('Type your new password:')
        for x in usersList:
            if x['password'] == currentUser['password']:
                x['password'] = new_info

def delete_user(user):
    for x in usersList:
        if x == user:
            usersList.remove(x)
            
def privacity(user):
    for x in usersList:
            if x['privacity'] == user['privacity']:
                x['privacity'] = 0

def add_member(new_member, group):
    group.append(new_member)


print('Welcome to RePros!')
print('Press c to create asn account')
print('Press e to edit your account info')
print('Press r to remove your account')
print('Press p to make your account private')
print('Press a to add a new member to the group')
print('Press q to quit')

action = input('What do you want to do? ')
action = action.lower()  # force lowercase
action = action[0]  # just use first letter
print()

if action == 'c':
    new_user()
    print(usersList[0], 'Seu usuário foi criado!!')
elif action == 'e':
    new_user()
    edit_user(usersList[0])
    print(usersList, 'Seu usuário foi editado!!')
elif action == 'p':
    privacity(usersList[0])
    print(usersList, 'O acesso ao perfil do seu usuário foi restringido!!')
elif action == 'a':
    # vamos criar um grupo exemplo pra mostrar a funcionalidade
    # da add_member
    # Também vamos considerar que temos dois membros iniciais
    new_user()
    new_user()

    group = []
    group.append(usersList[0])
    group.append(usersList[1])

    # vamos criar um usuário e colocá-lo
    new_user()
    add_member(usersList[2], group)

    print(groupsList, 'Seu novo membro foi adicionado!!')

elif action == 'r':
    # vamos adicionar um usuário e depois removê-lo
    new_user()
    delete_user(usersList[0])

    print(usersList, 'Seu usuário foir removido!!')


    
