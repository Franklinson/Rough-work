#!/user/bin/python3

class Users:
    def __init__(self, name, email, password, comfirm_password):
        self.name = name
        self.email = email
        self.pasword = password
        self.comfirm_password = comfirm_password

    def display(self):
        print(f"Name: {self.name}")