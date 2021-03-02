import json, os, random, requests

from kivy.graphics import Color
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import Screen


def generate_color():
    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
    return color
    
class UserPage(Screen):
    def __init__(self,**kwargs):
        super(UserPage, self).__init__(**kwargs)

    def getMood(self, event):
        random_color = get_color_from_hex(generate_color())
        if self.ids.moodInput.text.strip():
            self.ids.moodBtn.color = [1,1,1,1]
            self.ids.moodAlert.color = random_color
            self.ids.moodBtn.background_color = random_color
            url = "https://theysaidso.p.rapidapi.com/quote/search"
            querystring = {"query":self.ids.moodInput.text, "maxlength":"150","minlength":"70","language":"en"}
            headers = {
                'x-rapidapi-key': os.getenv("RAPID_API_KEY"),
                'x-rapidapi-host': "theysaidso.p.rapidapi.com"
                }
            response = requests.request("GET", url, headers=headers, params=querystring)
            quote = json.loads(response.text)["contents"]["quotes"][0]
            self.ids.moodAlert.text = quote["quote"] + "\n\n" + quote["author"]

    def logout(self, event):
        self.parent.current = "login"
    pass