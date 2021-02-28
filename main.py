import os

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from src.Login import LoginPage
from src.User import UserPage

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