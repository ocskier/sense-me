import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

users = [{
    "username": "tester",
    "password": "pwd"
}]

class LoginPage(Screen):
    def __init__(self,**kwargs):
        super(LoginPage, self).__init__(**kwargs)

    def runLogin(self, event):
        user_inpt = self.ids.userInput.text
        pass_inpt = self.ids.passInput.text
        for user in users:
            if user["username"] == user_inpt and user["password"] == pass_inpt:
                print("Logged In")
                self.parent.current = "user"
            else: 
                print("Invalid Credentials!!")
    pass

class UserPage(Screen):
    pass

class SenseMe(ScreenManager):
    pass

class SenseMeApp(App):
    def build(self):
        Builder.load_file(os.path.abspath(os.path.join(os.path.dirname(__file__),'sense-me.kv')))
        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginPage(name="login"))
        screen_manager.add_widget(UserPage(name="user"))
        screen_manager.current = "login"
        return screen_manager


if __name__ == '__main__':
    SenseMeApp().run()