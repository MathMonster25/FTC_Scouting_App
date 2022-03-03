from kivy.properties import StringProperty, BooleanProperty

from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from py_helpers.ScoringValue import ScoringValue

class TwoSwitchValue(ScoringValue):

    value1 = BooleanProperty()
    value2 = BooleanProperty()

    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)

        self.label = MDLabel()
        self.label.halign = "center"
        self.add_widget(self.label)



class ToggleButton(MDRectangleFlatButton, MDToggleButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = self.theme_cls.primary_light