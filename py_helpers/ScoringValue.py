from kivy.properties import StringProperty

from kivymd.uix.boxlayout import MDBoxLayout


class ScoringValue(MDBoxLayout):

    text = StringProperty()

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        self.orientation = "horizontal"
        self.padding = (5, 0)
        self.adaptive_height = True