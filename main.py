import os
# When commented out, debug lines get printed
#os.environ["KIVY_NO_CONSOLELOG"] = "1"

# Allows compiling for ios
xyz = os.path.join('~', 'Documents', 'your_directory')
os.environ["PYTHON_EGG_CACHE"] = os.path.expanduser(xyz)

# Kivy imports
import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import BooleanProperty
from kivy.core.window import Window
from kivy.metrics import inch

# Set window size to approx. size of iPhone XR (specific to Asus ROG G14 screen)
Window.size = (inch(828/326)*1.15, inch(1792/326)*1.15)

# KivyMD imports
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine

# Ensures compatibility with app if compiled on another computer
kivy.require("2.0.0")

# Custom class imports
from py_helpers.screens import *
from py_helpers.scoring_dropdowns import *
from py_helpers.BetterButton import BetterButton
from py_helpers.BetterLabel import BetterLabel
from py_helpers.ImageButton import ImageButton

class MainApp(MDApp):
    is_ios = BooleanProperty(ThemableBehavior.device_ios)
    started = False
    prev_screens = []

    autonomous = None
    teleop = None
    endgame = None

    score = 0

    def build(self):
        # Theming

        self.theme_cls.theme_style = "Dark"

        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "900"

        self.theme_cls.accent_palette = "Lime"
        self.theme_cls.accent_hue = "A700"

        # Load the main kv file, which contains a screen manager for all kv screens
        return Builder.load_file("main.kv")

    def on_start(self):
        self.autonomous = AutonomousDropDown(self)
        self.teleop = TeleOpDropDown(self)
        self.endgame = EndgameDropDown(self)
        scoring_dropdowns = [self.autonomous, self.teleop, self.endgame]
        for dropdown in scoring_dropdowns:
            panel = MDExpansionPanel(
                    icon="",
                    content=dropdown,
                    panel_cls=MDExpansionPanelOneLine(text=dropdown.title)
                )
            panel.bind(_state=self.rescroll)
            self.root.ids.score_sheet.ids.scoring_menu.add_widget(panel)

        self.root.ids.toolbar2.ids.label_title.font_size = "24sp"

        self.started = True

    def change_screen(self, screen_name: str, direction:str ="left"):
        """
        Transitions from current screen to new screen
        :param screen_name: The name of the new screen
        :param direction: If applicable, the direction of the transition
        """

        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager'] # type: ScreenManager
        if screen_name != "home_screen":
            self.prev_screens.append(screen_manager.current)
        else:
            self.prev_screens = []

        # Transition using the given direction
        screen_manager.transition.direction = direction
        screen_manager.current = screen_name

        if screen_name != "home_screen":
            self.root.ids.toolbar1.left_action_items = [["arrow-left-bold-circle", lambda x: self.move_back_screen()]]
        else:
            self.root.ids.toolbar1.left_action_items = [["menu"]]

    def move_back_screen(self):
        """
        Transitions from current screen to the previous screen
        """

        screen_name = self.prev_screens[-1]
        self.prev_screens.pop(-1)

        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']  # type: ScreenManager

        # Transition using the given direction
        screen_manager.transition.direction = "right"
        screen_manager.current = screen_name

        if screen_name != "home_screen":
            self.root.ids.toolbar1.left_action_items = [["arrow-left-bold-circle", lambda x: self.move_back_screen()]]
        else:
            self.root.ids.toolbar1.left_action_items = [["menu"]]

    def rescroll(self, *args):
        self.root.ids.score_sheet.ids.scroll_view.scroll_to(self.root.ids.score_sheet.ids.scoring_menu)

    def update_score(self, *args):
        if self.autonomous is None or self.teleop is None or self.endgame is None:
            return

        self.score = 0

        auto = self.autonomous # type: AutonomousDropDown
        self.score += (
                auto.high_goals.value * 12 +
                auto.mid_goals.value * 6 +
                auto.low_goals.value * 3 +
                auto.power_shots.value1 * 15 +
                auto.power_shots.value2 * 15 +
                auto.power_shots.value3 * 15 +
                auto.wobbles.value1 * 15 +
                auto.wobbles.value2 * 15 +
                auto.parked.value * 5
        )

        tele = self.teleop # type: TeleOpDropDown
        self.score += (
                tele.high_goals.value * 6 +
                tele.mid_goals.value * 4 +
                tele.low_goals.value * 2
        )

        end = self.endgame # type: EndgameDropDown
        self.score += (
                end.high_goals.value * 12 +
                end.mid_goals.value * 6 +
                end.low_goals.value * 3 +
                end.power_shots.value1 * 15 +
                end.power_shots.value2 * 15 +
                end.power_shots.value3 * 15 +
                end.wobbles_drop.value1 * 20 +
                end.wobbles_drop.value2 * 20 +
                end.wobbles_start.value1 * 5 +
                end.wobbles_start.value2 * 5 +
                end.wobble_rings.value * 5
        )

        self.root.ids.score_sheet.ids.score.text = "Score: " + str(self.score)

    def resetScore(self, *args):
        if self.autonomous is None or self.teleop is None or self.endgame is None:
            return

        auto = self.autonomous  # type: AutonomousDropDown
        auto.high_goals.reset()
        auto.mid_goals.reset()
        auto.low_goals.reset()
        auto.power_shots.reset()
        auto.wobbles.reset()
        auto.parked.reset()

        tele = self.teleop  # type: TeleOpDropDown
        tele.high_goals.reset()
        tele.mid_goals.reset()
        tele.low_goals.reset()

        end = self.endgame  # type: EndgameDropDown
        end.high_goals.reset()
        end.mid_goals.reset()
        end.low_goals.reset()
        end.power_shots.reset()
        end.wobbles_drop.reset()
        end.wobbles_start.reset()
        end.wobble_rings.reset()

    def getToolbarHeight(self):
        if self.started:
            return self.root.ids.toolbar1.height + self.root.ids.toolbar2.height
        else:
            return 0

if __name__ == "__main__":
    # Start the app
    app = MainApp()
    app.run()