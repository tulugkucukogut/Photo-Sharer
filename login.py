from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('login.kv')
class LoginScreen(Screen):
    #hey
    pass

class RootWidget(ScreenManager):
    pass

class Login(App):
    def build(self):
        return RootWidget()
    
Login().run()


