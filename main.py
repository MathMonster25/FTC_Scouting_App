from time import time
import os
# When commented out, debug lines get printed
#os.environ["KIVY_NO_CONSOLELOG"] = "1"
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.properties import StringProperty

# Ensures compatibility with app if compiled on another computer
kivy.require("2.0.0")

class BetterButton(Button):

    button_unpressed_color = None
    button_pressed_color = None
    text_unpressed_color = None
    text_pressed_color = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = "./icons/white_background.png"
        self.background_down = "./icons/white_background.png"

        self.markup = True

        self.button_unpressed_color = self.background_color
        self.button_pressed_color = self.background_color
        self.text_unpressed_color = self.color
        self.text_pressed_color = self.color

    def _do_press(self):
        super()._do_press()
        self.color = self.text_pressed_color
        self.background_color = self.button_pressed_color

    def _do_release(self, *args):
        super()._do_release(*args)
        self.color = self.text_unpressed_color
        self.background_color = self.button_unpressed_color

class HomeScreen(Screen):
    pass

class SelectTeam(Screen):
    pass

class AddTeam(Screen):
    pass

class ScoreSheet(Screen):
    pass

class MainApp(App):
    def build(self):
        # Load the main kv file, which contains a screen manager for all kv screens
        return Builder.load_file("main.kv")

    def change_screen(self, screen_name: str, direction:str ="left"):
        """
        Transitions from current screen to new screen
        :param screen_name: The name of the new screen
        :param direction: If applicable, the direction of the transition
        """

        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager'] # type: ScreenManager

        # Transition using the given direction
        screen_manager.transition.direction = direction
        screen_manager.current = screen_name

if __name__ == "__main__":
    # Start the app
    app = MainApp()
    app.run()