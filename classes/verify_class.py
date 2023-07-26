class VerifyUser():
    
    def verify_login(self, users, user_login):
        for user in users:
            if user_login == user.get_user_login():
                return True
        return False
    
    def verify_nickname(self, users, user_nickname):
        for user in users:
            if user_nickname == user.get_user_nickname():
                return True
        return False
