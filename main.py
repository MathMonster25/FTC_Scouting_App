import os
# When commented out, debug lines get printed
#os.environ["KIVY_NO_CONSOLELOG"] = "1"
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
# Ensures compatibility with app if compiled on another computer
kivy.require("2.0.0")

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

    def change_screen(self, screen_name, direction="left"):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager'] # type: ScreenManager

        # Transition using the given direction
        screen_manager.transition.direction = direction
        screen_manager.current = screen_name

if __name__ == "__main__":
    chat_app = MainApp()
    chat_app.run()