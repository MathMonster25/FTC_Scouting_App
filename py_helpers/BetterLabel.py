from kivy.properties import ListProperty, NumericProperty
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color

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