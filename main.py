from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.animation import Animation

from kivy.uix.boxlayout import BoxLayout

path = "assets/"

class ContentNavDrawer(BoxLayout):
    pass

class BaseApp(MDApp):

    chat = path+"collab.png"
    message = path+"message.png"
    transfer = path+"transfer.png"
    security = path+"security.png"

    def __init__(self,**kwargs):
        super(BaseApp,self).__init__(**kwargs)
        pass


    def animate_cards(self,widget):
        animate = Animation(pos_x=-100,duration=3)
        animate.start(widget)

    def on_start(self):
        pass



    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("intro.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))

        return screen_manager


if __name__ == "__main__":
    BaseApp().run()