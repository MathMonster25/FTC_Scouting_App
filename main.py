import os
# When commented out, debug lines get printed
os.environ["KIVY_NO_CONSOLELOG"] = "1"

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
    penalties = None

    auto_low = 0
    auto_middle = 0
    auto_high = 0

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
        self.penalties = PenaltiesDropDown(self)

        scoring_dropdowns = [self.autonomous, self.teleop, self.endgame]
        for dropdown in scoring_dropdowns:
            panel = MDExpansionPanel(
                    icon="",
                    content=dropdown,
                    panel_cls=MDExpansionPanelOneLine(text=dropdown.title)
                )
            panel.bind(_state=self.rescroll)
            panel.panel_cls.bind(text=dropdown.get_title)
            self.root.ids.score_sheet.ids.scoring_menu.add_widget(panel)

        penalty_panel = MDExpansionPanel(
            icon = "",
            content = self.penalties,
            panel_cls = MDExpansionPanelOneLine(text=self.penalties.title)
        )
        penalty_panel.bind(_state=self.rescroll)
        self.root.ids.score_sheet.ids.penalties_menu.add_widget(penalty_panel)

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
        if screen_name != "score_sheet":
            self.prev_screens.append(screen_manager.current)
        else:
            self.prev_screens = []

        # Transition using the given direction
        screen_manager.transition.direction = direction
        screen_manager.current = screen_name

        if screen_name != "score_sheet":
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

        if screen_name != "score_sheet":
            self.root.ids.toolbar1.left_action_items = [["arrow-left-bold-circle", lambda x: self.move_back_screen()]]
        else:
            self.root.ids.toolbar1.left_action_items = [["menu"]]

    def rescroll(self, *args):
        self.root.ids.score_sheet.ids.scroll_view.scroll_to(self.root.ids.score_sheet.ids.scoring_menu)

    def update_score(self, *args):
        if self.autonomous is None or self.teleop is None or self.endgame is None or self.penalties is None:
            return

        auto = self.autonomous # type: AutonomousDropDown
        auto_score = (
                auto.duck.value * 10 +
                auto.unit.value * 2 +
                (auto.low.value + auto.middle.value + auto.high.value) * 6 +
                auto.duck_bonus.value1 * 10 +
                auto.duck_bonus.value2 * 10 +
                auto.tse_bonus.value1 * 20 +
                auto.tse_bonus.value2 * 20
        )

        auto.title = "Autonomous: " + str(auto_score)

        tele = self.teleop # type: TeleOpDropDown

        low_dif = auto.low.value - self.auto_low
        middle_dif = auto.middle.value - self.auto_middle
        high_dif = auto.high.value - self.auto_high

        self.auto_low = auto.low.value
        self.auto_middle = auto.middle.value
        self.auto_high = auto.high.value

        tele_score = (
                tele.unit.value * 1 +
                tele.shared.value * 4 +
                (tele.low.value + low_dif) * 2 +
                (tele.middle.value + middle_dif) * 4 +
                (tele.high.value + high_dif) * 6
        )

        tele.title = "Tele-Op: " + str(tele_score)

        end = self.endgame # type: EndgameDropDown
        end_score = (
                end.ducks.value * 6 +
                end.balanced.value * 10 +
                end.tipped.value * 20 +
                end.capped.value1 * 15 +
                end.capped.value2 * 15
        )

        end.title = "Endgame: " + str(end_score)

        pen = self.penalties # type: PenaltiesDropDown
        pen_score = (
            pen.minors.value * 10 +
            pen.majors.value * 30
        )

        pen.title = "Penalties: " + str(-pen_score)

        self.score = auto_score + tele_score + end_score - pen_score

        self.root.ids.score_sheet.ids.score.text = "Score: " + str(self.score)

        tele.low.add(low_dif)
        tele.middle.add(middle_dif)
        tele.high.add(high_dif)

    def resetScore(self, *args):
        if self.autonomous is None or self.teleop is None or self.endgame is None:
            return

        auto = self.autonomous  # type: AutonomousDropDown
        auto.reset()

        self.auto_low = 0
        self.auto_middle = 0
        self.auto_high = 0

        tele = self.teleop  # type: TeleOpDropDown
        tele.reset()

        end = self.endgame  # type: EndgameDropDown
        end.reset()

        pen = self.penalties # type: PenaltiesDropDown
        pen.reset()

        self.score = 0
        self.root.ids.score_sheet.ids.score.text = "Score: " + str(self.score)

    def getToolbarHeight(self):
        if self.started:
            return self.root.ids.toolbar1.height + self.root.ids.toolbar2.height
        else:
            return 0



if __name__ == "__main__":
    # Start the app
    app = MainApp()
    app.run()