from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.boxlayout import MDBoxLayout

class SingleCheckValue(MDBoxLayout):

    text = StringProperty()
    value = BooleanProperty(False)

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        self.orientation = "horizontal"
        self.padding = (5, 0)
        self.adaptive_height = True

        self.label = MDLabel()
        self.label.halign = "center"
        self.add_widget(self.label)

        self.add_widget(PlaceHolder())

        self.check = Check(self.update_value)
        checkAnchor = AnchorLayout()
        checkAnchor.add_widget(self.check)
        checkAnchor.anchor_x = "center"
        self.add_widget(checkAnchor)
        checkAnchor.size_hint_x = 0.2

        self.add_widget(PlaceHolder())

        self.bind(text=self.update_text)

    def update_value(self, *args):
        self.value = self.check.active
        self.app.update_score()

    def update_text(self, *args):
        self.label.text = self.text

    def reset(self):
        self.check.active = False

class DoubleCheckValue(MDBoxLayout):

    text = StringProperty()
    value1 = BooleanProperty(False)
    value2 = BooleanProperty(False)

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        self.orientation = "horizontal"
        self.padding = (5, 0)
        self.adaptive_height = True

        self.label = MDLabel()
        self.label.halign = "center"
        self.add_widget(self.label)

        self.check1 = Check(self.update_value1)
        self.add_widget(self.check1)

        self.add_widget(MDLabel(size_hint_x = 0.2))

        self.check2 = Check(self.update_value2)
        self.add_widget(self.check2)

        self.bind(text=self.update_text)

    def update_value1(self, *args):
        self.value1 = self.check1.active
        self.app.update_score()

    def update_value2(self, *args):
        self.value2 = self.check2.active
        self.app.update_score()

    def update_text(self, *args):
        self.label.text = self.text

    def reset(self):
        self.check1.active = False
        self.check2.active = False

class TripleCheckValue(MDBoxLayout):

    text = StringProperty()
    value1 = BooleanProperty(False)
    value2 = BooleanProperty(False)
    value3 = BooleanProperty(False)

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        self.orientation = "horizontal"
        self.padding = (5, 0)
        self.adaptive_height = True

        self.label = MDLabel()
        self.label.halign = "center"
        self.add_widget(self.label)

        self.check1 = Check(self.update_value1)
        self.add_widget(self.check1)

        self.check2 = Check(self.update_value2)
        self.check2.size = ("36dp", "36dp")
        checkAnchor = AnchorLayout()
        checkAnchor.add_widget(self.check2)
        checkAnchor.anchor_x = "center"
        self.add_widget(checkAnchor)
        checkAnchor.size_hint_x = 0.2

        self.check3 = Check(self.update_value3)
        self.add_widget(self.check3)

        self.bind(text=self.update_text)

    def update_value1(self, *args):
        self.value1 = self.check1.active
        self.app.update_score()

    def update_value2(self, *args):
        self.value2 = self.check2.active
        self.app.update_score()

    def update_value3(self, *args):
        self.value3 = self.check2.active
        self.app.update_score()

    def update_text(self, *args):
        self.label.text = self.text

    def reset(self):
        self.check1.active = False
        self.check2.active = False
        self.check3.active = False

class Check(MDCheckbox):

    def __init__(self, update_method, **kwargs):
        super().__init__(**kwargs)
        self.update_method = update_method

        self.size_hint = (None, None)
        self.size = ("48dp", "48dp")
        self.pos_hint = {"center_y": 0.5}

        self.selected_color = self.unselected_color

        self.bind(active=self.update_method)

class PlaceHolder(MDIcon):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.icon = ""

        self.size = ("48dp", "48dp")
        self.adaptive_size = True