from kivy.uix.image import Image
from kivy.properties import StringProperty
from .BetterButton import BetterButton

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