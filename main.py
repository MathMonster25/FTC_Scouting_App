from time import time
import os
# When commented out, debug lines get printed
#os.environ["KIVY_NO_CONSOLELOG"] = "1"
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.properties import ListProperty, BooleanProperty, NumericProperty
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color

# Ensures compatibility with app if compiled on another computer
kivy.require("2.0.0")

class BetterButton(Button):

    button_unpressed_color = ListProperty()
    button_pressed_color = ListProperty()
    text_unpressed_color = ListProperty()
    text_pressed_color = ListProperty()

    b_state = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_down = ""

        self.markup = True

        self.button_unpressed_color = self.background_color
        self.button_pressed_color = self.background_color
        self.text_unpressed_color = self.color
        self.text_pressed_color = self.color

    def do_press(self):
        self.color = self.text_pressed_color
        self.background_color = self.button_pressed_color

    def do_release(self):
        self.color = self.text_unpressed_color
        self.background_color = self.button_unpressed_color

    def _do_press(self):
        super()._do_press()
        self.b_state = True
        self.do_press()

    def _do_release(self, *args):
        super()._do_release(*args)
        self.b_state = False
        self.do_release()

class BetterLabel(Label):

    border_color_rgba = ListProperty()
    rect_color_rgba = ListProperty()
    border_thickness = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.border_color_rgba = (0, 0, 0, 0)
        self.rect_color_rgba = (0, 0, 0, 1)
        self.border_thickness = 0

        with self.canvas:
            self.border_color = Color(rgba=self.border_color_rgba)
            self.border = Rectangle(pos = self.pos, size = self.size)
            self.rect_color = Color(rgba=self.rect_color_rgba)
            self.rect = Rectangle(pos = (self.pos[0] + self.border_thickness, self.pos[1] + self.border_thickness),
                                  size = (self.size[0] - self.border_thickness, self.size[1] - self.border_thickness))

        self.bind(pos=self.update_rect, size=self.update_rect,
                  rect_color_rgba=self.update_rect, border_color_rgba=self.update_rect,
                  border_thickness=self.update_rect)

    def update_rect(self, *args):
        self.border_color.rgba = self.border_color_rgba
        self.border.pos = self.pos
        self.border.size = self.size
        self.rect_color.rgba = self.rect_color_rgba
        self.rect.pos = (self.pos[0] + self.border_thickness, self.pos[1] + self.border_thickness)
        self.rect.size = (self.size[0] - self.border_thickness, self.size[1] - self.border_thickness)

class HomeScreen(Screen):
    def on_enter(self, *args):
        super().on_enter(*args)

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