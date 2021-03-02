import json
from kivy.uix.screenmanager import Screen

class SignUpPage(Screen):
    def __init__(self,**kwargs):
        super(SignUpPage, self).__init__(**kwargs)

    def changePage(self, event):
        self.ids.alertTwo.size_hint_y = 0
        self.parent.current = "login"

    def runRegister(self, event):
        user_input = self.ids.newUserInput.text
        pass_input = self.ids.newPassInput.text
        with open("./db/users.json", "r") as f:
            data = json.load(f)
            if user_input.strip() and pass_input.strip():
                data["users"].append({"username": user_input,"password": pass_input})
                print(data["users"])
                with open("./db/users.json", "w") as fw:
                    json.dump(data, fw)
                    print("Sign Up successful!")
                    self.parent.current = "login"
            else: 
                self.ids.alertTwo.size_hint_y = 0.2
                self.ids.alertLabelTwo.text = "Invalid Credentials!!"
    pass