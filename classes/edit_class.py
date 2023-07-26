from verify_class import VerifyUser

class EditUser():
    
    def edit_login(self, users, user_login):
        new_user_login = input('\nDigite seu novo login: ')

        verify = VerifyUser()
        if verify.verify_login(users, new_user_login):
            print('Esse login ja existe')
            return user_login
        else:
            
    
    def edit_nickname(self, users, user_login):
        new_user_nickname = input('\nDigite seu novo nickname: ')

        verify = VerifyUser()
        if verify.verify_nickname(users, new_user_nickname):
            print('\nEsse nickname ja existe')
            return user_login




    