import os
from colorutils import random_web
from kivy.app import App
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen

users = [{
    "username": "tester",
    "password": "pwd"
}]

class LoginPage(Screen):
    def __init__(self,**kwargs):
        super(LoginPage, self).__init__(**kwargs)

    def runLogin(self, event):
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

class UserPage(Screen):
    def __init__(self,**kwargs):
        super(UserPage, self).__init__(**kwargs)

    def getMood(self, event):
        self.ids.moodBtn.background_color = get_color_from_hex(random_web())
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