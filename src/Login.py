from kivy.uix.screenmanager import Screen

class LoginPage(Screen):
    def __init__(self,**kwargs):
        super(LoginPage, self).__init__(**kwargs)

    def runLogin(self, event):
        users = [{
            "username": "tester",
            "password": "pwd"
        }]
        user_input = self.ids.userInput.text
        pass_input = self.ids.passInput.text
        for user in users:
            if user["username"] == user_input and user["password"] == pass_input:
                self.ids.alert.size_hint_y = 0
                print("Logged In")
                self.parent.current = "user"
            else: 
                self.ids.alert.size_hint_y = 0.2
                self.ids.alertLabel.text = "Invalid Credentials!!"
    pass