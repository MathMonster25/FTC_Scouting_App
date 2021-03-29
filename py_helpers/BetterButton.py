from kivy.uix.button import Button
from kivy.properties import ListProperty, BooleanProperty

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