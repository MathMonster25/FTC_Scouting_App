from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel

from py_helpers.ScoringValue import ScoringValue

class IncrementValue(ScoringValue):

    value = NumericProperty(0)
    app = ObjectProperty()

    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)

        self.label = MDLabel()
        self.label.halign = "center"
        self.label.adaptive_width = False
        self.add_widget(self.label)

        self.minusButton = MinusButton(self)
        self.add_widget(self.minusButton)

        self.valueLabel = MDLabel(text=str(self.value))
        self.valueLabel.halign = "center"
        self.valueLabel.pos_hint = {"center_y": 0.5}
        self.add_widget(self.valueLabel)
        self.valueLabel.size_hint_x = 0.2

        self.addButton = AddButton(self)
        self.add_widget(self.addButton)

        self.bind(text=self.changeText)
        self.bind(value=self.changeValue)

    def changeText(self, *args):
        self.label.text = self.text

    def changeValue(self, *args):
        self.valueLabel.text = str(self.value)
        if self.app is not None:
            self.app.update_score()

    def add(self, value=1):
        self.value += value

    def minus(self):
        if self.value > 0:
            self.value -= 1

    def reset(self):
        self.value = 0

class AddButton(MDIconButton):

    def __init__(self, increment_button: IncrementValue, **kwargs):
        super().__init__(**kwargs)
        self.increment_button = increment_button
        self.icon = "plus-circle"

    def on_press(self):
        super().on_press()
        self.increment_button.add()

class MinusButton(MDIconButton):

    def __init__(self, increment_button: IncrementValue, **kwargs):
        super().__init__(**kwargs)
        self.increment_button = increment_button
        self.icon = "minus-circle"

    def on_press(self):
        super().on_press()
        self.increment_button.minus()