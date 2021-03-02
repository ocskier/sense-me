import json
from kivy.uix.screenmanager import Screen

class LoginPage(Screen):
    def __init__(self,**kwargs):
        super(LoginPage, self).__init__(**kwargs)

    def changePage(self, event):
        self.ids.alert.size_hint_y = 0
        self.parent.current = "sign_up"
    
    def runLogin(self, event):
        user_input = self.ids.userInput.text
        pass_input = self.ids.passInput.text
        with open("./db/users.json") as f:
            data = json.load(f)
            if len(data["users"]) == 0:
                self.ids.alert.size_hint_y = 0.3
                self.ids.alertLabel.text = "Invalid Credentials!!"
            else: 
                for user in data["users"]:
                    if user["username"] == user_input and user["password"] == pass_input:
                        self.ids.alert.size_hint_y = 0
                        print("Logged In")
                        self.parent.current = "user"
                    else: 
                        self.ids.alert.size_hint_y = 0.3
                        self.ids.alertLabel.text = "Invalid Credentials!!"
    pass