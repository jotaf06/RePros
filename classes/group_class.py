class Group():
    def __init__(self, group_name):
        self.group_name = group_name
        self.group_members = []
        self.group_files = [] 

    def get_group_name(self):
        return self.group_name
    
    def get_group_members(self):
        return self.group_members
    
    def get_group_files(self):
        return self.group_files
    
    def entrar_grupo(self, user_nickname):
    
    def add_group_member(self, user_nickname):
        self.group_members.append(user_nickname)
