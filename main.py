import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"
import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require("2.0.0")

class MainApp(App):
    def build(self):
        return Label(text="Hello World!")

if __name__ == "__main__":
    chat_app = MainApp()
    chat_app.run()
