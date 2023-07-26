class User():
    def __init__(self, user_login, user_nickname, user_password, user_privacity):
        self.user_login = user_login
        self.user_nickname = user_nickname
        self.user_password = user_password
        self.user_privacity = user_privacity
    
    def get_user_login(self):
        return self.user_login

    def get_user_nickname(self):
        return self.user_nickname
    
    def get_user_password(self):
        return self.user_password

    def get_user_privacity(self):
        return self.user_privacity

    def __str__(self):
        return f"Login: {self.user_login}\nNickname: {self.user_nickname}\nPassword: {self.user_password}\nPrivacity: {self.user_privacity}\n"