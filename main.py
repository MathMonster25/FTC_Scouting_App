import os
# When commented out, debug lines get printed
#os.environ["KIVY_NO_CONSOLELOG"] = "1"
# Allows compiling for ios
is_ios = True
if is_ios:
    xyz = os.path.join('~', 'Documents', 'your_directory')
    os.environ["PYTHON_EGG_CACHE"] = os.path.expanduser(xyz)
import kivy
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.button import Button
from kivy.properties import ListProperty, BooleanProperty, NumericProperty, StringProperty
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color

from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine

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

class ImageButton(BetterButton):

    image_unpressed = StringProperty()
    image_pressed = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.text_unpressed_color = (0, 0, 0, 0)
        self.text_pressed_color = (0, 0, 0, 0)
        self.color = (0, 0, 0, 0)
        self.button_unpressed_color = (0, 0, 0, 0)
        self.button_pressed_color = (0, 0, 0, 0)
        self.background_color = (0, 0, 0, 0)

        self.image = Image(source = "", pos = self.pos)
        self.image.allow_stretch = True
        self.image.keep_ratio = False
        self.add_widget(self.image)
        self.bind(image_unpressed=self.create_image, pos=self.update_pos, size=self.update_pos)

    def create_image(self, *args):
        if not self.b_state:
            self.image.source = self.image_unpressed
        else:
            self.image.source = self.image_pressed

        self.image.pos = self.pos

    def update_pos(self, *args):
        self.image.pos = self.pos
        self.image.size = self.size

    def do_press(self):
        self.image.source = self.image_pressed

    def do_release(self):
        self.image.source = self.image_unpressed

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

class HomeScreen(MDScreen):
    pass

class SelectTeam(MDScreen):
    pass

class AddTeam(MDScreen):
    pass

class ScoreSheet(MDScreen):
    pass

class AutonomousDropDown(MDBoxLayout):
    title="Autonomous:"

class TeleOpDropDown(MDBoxLayout):
    title="Tele-Op:"

class EndgameDropDown(MDBoxLayout):
    title="Endgame:"

class MainApp(MDApp):
    is_ios = BooleanProperty(ThemableBehavior.device_ios)
    started = False

    def build(self):
        # Theming

        self.theme_cls.theme_style = "Light"

        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "900"

        self.theme_cls.accent_palette = "Lime"
        self.theme_cls.accent_hue = "A700"

        # Load the main kv file, which contains a screen manager for all kv screens
        return Builder.load_file("main.kv")

    def on_start(self):
        scoring_dropdowns = [AutonomousDropDown(), TeleOpDropDown(), EndgameDropDown()]
        for dropdown in scoring_dropdowns:
            self.root.ids.score_sheet.ids.scoring_menu.add_widget(
                MDExpansionPanel(
                    icon="",
                    content=dropdown,
                    panel_cls=MDExpansionPanelOneLine(text=dropdown.title)
                )
            )

        self.started = True

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

    def getToolbarHeight(self):
        if self.started:
            return self.root.ids.toolbar.height
        else:
            return 0

if __name__ == "__main__":
    # Start the app
    app = MainApp()
    app.run()