from colorutils import random_web
from kivy.utils import get_color_from_hex

from kivy.uix.screenmanager import Screen

class UserPage(Screen):
    def __init__(self,**kwargs):
        super(UserPage, self).__init__(**kwargs)

    def getMood(self, event):
        self.ids.moodBtn.background_color = get_color_from_hex(random_web())
    
    def logout(self, event):
        self.parent.current = "login"
    pass