import json

class SaveOperations():
    def save_users(self, users):
        with open('users.json', 'w') as file:
            json.dump(users, file, indent=4)

    def save_groups(self, groups):
        with open('groups.json', 'w') as file:
            json.dump(groups, file, indent=4)

    def save_relationship(self, relationship):
        with open('amigos.json', 'w') as file:
            json.dump(relationship, file, indent=4)

    def load_users(self):
        with open('users.json', 'r') as file:
            return json.load(file)
        
    def load_groups(self):
        with open('groups.json', 'r') as file:
            return json.load(file)
        
    def load_relationship(self):
        with open('amigos.json', 'r') as file:
            return json.load(file)

    